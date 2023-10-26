import psutil
from .verdict import Verdict

class ExecutionResult:
  def __init__(self, verdict: Verdict or None, runtime):
    self.runtime = runtime
    self.verdict = verdict
    self.score = None

  def is_tle(self):
    return self.verdict == Verdict.TLE

  def is_error(self):
    return self.verdict == Verdict.RTE or self.verdict == Verdict.TLE
  
  def update_verdict(self, verdict: Verdict, score: int or None):
    assert(self.verdict == None and verdict != None)
    self.verdict = verdict
    self.score = score