import argparse
import yaml
import os

# Create the argument parser
parser = argparse.ArgumentParser()

# Add a flag argument
parser.add_argument('-v', '--verbose', help='will also print error message if rte', action="store_true")
parser.add_argument('-b', '--brief', help='only print the results', action="store_true")
parser.add_argument("--beta-mode", help="beta mode, uses cpu time to measure time limit", action="store_true")
parser.add_argument("--executable", help="path to executable solution, will override solution", default=None, required=False)
parser.add_argument("--solution", help="solution file path", default="./solution.cpp", required=False)
parser.add_argument("--scorer", help="scorer file path", default="./helper/scorer.cpp", required=False)
parser.add_argument("--test-dir", help="directory containing test cases", default="./tests", required=False)

# Parse the command-line arguments
args = parser.parse_args()

# Parsing yaml config
with open('./config.yml', 'r') as file:
  judge_config = yaml.safe_load(file)

class Config:
  COMPILE_FLAG = judge_config['compile_flag']
  TIME_LIMIT = judge_config['time_limit']
  REAL_TIME_LIMIT = judge_config['user_time_limit']
  SCORER_TIME_LIMIT = judge_config['scorer_time_limit']
  VERBOSE = args.verbose
  BRIEF = args.brief
  BETA_MODE = args.beta_mode
  EXECUTABLE_PATH = args.executable

  CON_CPP_PATH = args.solution
  SCORER_CPP_PATH = args.scorer

  CON_OUTPUT_PATH = "./temp/contestant"
  CON_SOLUTION_PATH = "./temp/solution.exe"
  SCORER_PATH = "./temp/scorer.exe"

  if EXECUTABLE_PATH != None:
    CON_SOLUTION_PATH = EXECUTABLE_PATH

  TESTCASES_PATH = args.test_dir

def initiate_directories():
  os.makedirs(Config.TESTCASES_PATH, exist_ok=True)
  os.makedirs(Config.CON_OUTPUT_PATH, exist_ok=True)

initiate_directories()
