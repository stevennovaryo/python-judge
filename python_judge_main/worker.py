import subprocess
import psutil
import time

from python_judge_main.result import ExecutionResult

from .config import Config
from .verdict import Verdict
from .logger import Logger

class Execution():

  def __init__(self, *args, **kwargs):
    self.process = subprocess.Popen(*args, **kwargs)
    if Config.BETA_MODE:
      self.psutil = psutil.Process(self.process.pid)
    else:
      self.psutil = None
    self.start_time = time.time()
    self.cpu_time = 0
    self.max_memory_usage = 0
    self.output = ''

  def return_result(self, verdict: Verdict):
    self.process.terminate()
    return ExecutionResult(verdict, self.cpu_time)

  def wait_cpu_time(self, time_limit: int):
    try:
      while self.process.poll() is None:
        self.cpu_time = self.psutil.cpu_times().system * 1000
        if self.cpu_time > time_limit:
          return self.return_result(Verdict.TLE)
        if (time.time() - self.start_time) * 1000 > Config.REAL_TIME_LIMIT:
          return self.return_result(Verdict.TLE) # TODO: Possible to add new verdict (User Time Limit Exceeded)  for this
    except subprocess.CalledProcessError as e:
      Logger().runtime_error(e.stderr.decode())
      return self.return_result(Verdict.RTE)
    except psutil.NoSuchProcess:
      pass

    self.output, error_output = self.process.communicate()

    if self.process.returncode != 0 or error_output:
      Logger().runtime_error(error_output)
      return self.return_result(Verdict.RTE)

    return self.return_result(None) # TODO: Possible to add new verdict (Unknown) for this

  def wait_real_time(self, real_time_limit: int):
    try:
      self.process.wait(real_time_limit)
    except subprocess.CalledProcessError as e:
      runtime = time.time() - self.start_time
      Logger().runtime_error(e.stderr.decode())
      return ExecutionResult(Verdict.RTE, runtime*1000)
    except subprocess.TimeoutExpired:
      runtime = time.time() - self.start_time
      self.process.terminate()
      return ExecutionResult(Verdict.TLE, runtime*1000)

    runtime = time.time() - self.start_time
    self.output, error_output = self.process.communicate()

    if self.process.returncode != 0 or error_output:
      Logger().runtime_error(error_output)
      return ExecutionResult(Verdict.RTE, runtime*1000)

    return ExecutionResult(None, runtime*1000)
  
  def wait(self, time: int):
    if Config.BETA_MODE:
      return self.wait_cpu_time(time)
    else:
      return self.wait_real_time(time / 1000)

def run_contestant_solution(input_file, con_output):
  """
    Runs and waits for the solution to finish within the time limit, currently using realtime. 
    Returns ExecutionResult with verdict if the solution does not TLE (time limit exceeded) or RTE (runtime error), 
    otherwise returns without verdict.
  """
  execution = Execution([Config.CON_SOLUTION_PATH], stdin=input_file, stdout=con_output, stderr=subprocess.PIPE)
  if Config.BETA_MODE:
    execution_result = execution.wait(Config.TIME_LIMIT)
  else:
    execution_result = execution.wait_real_time(Config.REAL_TIME_LIMIT / 1000)

  con_output.flush()
  return execution_result

def judge(input_name, input_path, output_path):
  input_file = open(input_path, 'r')
  con_output_path = Config.CON_OUTPUT_PATH + f'/{input_name}'
  con_output = open(con_output_path, 'w+')

  executionResult = run_contestant_solution(input_file, con_output)
  if executionResult.is_error():
    print_verdict(input_name, executionResult)
    return executionResult

  scorer = Execution([Config.SCORER_PATH, input_path, output_path, con_output_path], stdout=subprocess.PIPE)
  scorer_execution_result = scorer.wait_real_time(Config.SCORER_TIME_LIMIT)

  if scorer_execution_result.is_error():
    Logger().error(f'scorer {scorer_execution_result.verdict} while running for: {input_name}')
    exit(1) # TODO implement handling

  update_scorer_verdict(scorer.output, executionResult)
  print_verdict(input_name, executionResult)

  return executionResult

def update_scorer_verdict(scorer_output, executionResult: ExecutionResult):
  scorer_output = scorer_output.decode("utf-8").split()
  code = scorer_output[0]
  score = int(scorer_output[1]) if scorer_output[0] == 'OK' else None  

  executionResult.update_verdict(Verdict[code], score)

def print_verdict(name, executionResult: ExecutionResult):
  Verdict.add_result(executionResult.verdict)

  runtime = executionResult.runtime
  verdict = executionResult.verdict
  score = executionResult.score

  if score == None:
    Logger().info(f'{name}: {verdict} {runtime:.0f} ms')
  else:
    Logger().info(f'{name}: {verdict}({score}) {runtime:.0f} ms')
