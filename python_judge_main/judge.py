import os
import subprocess

from . import worker
from .config import Config
from .logger import Logger
from .verdict import Verdict


def compile():
  flag = Config.COMPILE_FLAG.split()
  Logger().print('compiling..')
  subprocess.run([*flag, '-o', Config.CON_SOLUTION_PATH, Config.CON_CPP_PATH])
  subprocess.run([*flag, '-o', Config.SCORER_PATH, Config.SCORER_CPP_PATH])
  Logger().print('compile success\n')

def judge_all_testcases():
  Logger().print('judging all testcases..')
  for file in os.listdir(Config.TESTCASES_PATH):
    if file[-3:] == '.in':
      input_path = Config.TESTCASES_PATH + f"/{file}"
      output_path = Config.TESTCASES_PATH + f"/{file[:-3]}.out"
      worker.judge(file, input_path, output_path)
  Verdict.print_verdict()
