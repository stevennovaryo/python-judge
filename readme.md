Used to test solution and scorer based on public test data. 

```bash
usage: main.py [-h] [-v] [-b] [--beta-mode] [--solution SOLUTION] [--scorer SCORER] [--test-dir TEST_DIR] [--config CONFIG]

optional arguments:
  -h, --help           show this help message and exit
  -v, --verbose        will also print error message if rte
  -b, --brief          only print the results
  --beta-mode          beta mode, uses cpu time to measure time limit
  --solution SOLUTION  solution file path
  --scorer SCORER      scorer file path
  --test-dir TEST_DIR  directory containing test cases
  --config CONFIG      config file path
```

## Installation for Global Call

1. Clone this repository and navigate to the directory.

2. Enable execution permissions on `start.sh`

```
chmod +x start.sh
```

3. Add the following alias to `~/.bashrc`. Change `~/path/to/python-judge/` to the path where the repository directory is located.

```
alias "python-judge"="~/path/to/python-judge/start.sh"
```

