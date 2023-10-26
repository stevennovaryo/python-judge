from enum import Enum
import sys

from .config import Config
from .logger import Logger


class VerdictCounter:
  verdict = {
    'TLE': 0,
    'WA': 0,
    'RTE': 0,
    'OK': 0,
    'AC': 0,
  }

class Verdict(Enum):
  OK = 'OK'
  AC = 'AC'
  WA = 'WA'
  TLE = 'TLE'
  RTE = 'RTE'

  def __str__(self):
    if sys.stdout.isatty():
      if self.value == 'AC':
        return f'\033[92;1m{self.value}\033[0m' # green color
      elif self.value == 'OK' or self.value == 'TLE' or self.value == 'RTE':
        return f'\033[33m{self.value}\033[0m' # yellow color 
      elif self.value == 'WA':
        return f'\033[31;1m{self.value}\033[0m' # red color
    
    return self.value

  def add_result(verdict):
    VerdictCounter().verdict[verdict.value] += 1

  def get_solution_path_string():
    if sys.stdout.isatty():
      return f'\033[33;1m\"{Config.CON_CPP_PATH}\"\033[0m'
    return f'\"{Config.CON_CPP_PATH}\"'
  
  def print_verdict():
    Logger().print('='*50)
    Logger().print(f'Execution for {Verdict.get_solution_path_string()} finished')
    Logger().print(f'Judging result:')
    Logger().print(f"{Verdict.OK}  : {VerdictCounter.verdict['OK']: >3}")
    Logger().print(f"{Verdict.AC}  : {VerdictCounter.verdict['AC']: >3}")
    Logger().print(f"{Verdict.WA}  : {VerdictCounter.verdict['WA']: >3}")
    Logger().print(f"{Verdict.TLE} : {VerdictCounter.verdict['TLE']: >3}")
    Logger().print(f"{Verdict.RTE} : {VerdictCounter.verdict['RTE']: >3}")
    Logger().print('='*50)
    