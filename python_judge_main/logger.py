import sys
from .config import Config

class Logger:

  def _wrap_error(self, message):
    if sys.stdout.isatty():
      return f'\033[31;1m{message}\033[0m' # red color
    return message

  def info(self, *args, **kwargs):
    if not Config.BRIEF:
      print(*args, **kwargs)

  def runtime_error(self, *args, **kwargs):
    if Config.VERBOSE:
      print(self._wrap_error('[RUNTIME ERROR]'), *args, **kwargs)

  def error(self, *args, **kwargs):
    print(self._wrap_error('[ERROR]'), *args, **kwargs)

  def print(self, *args, **kwargs):
    print(*args, **kwargs)
