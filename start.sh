#!/usr/bin/bash

param=()

for var in "$@"; do
  if ! [[ $var == "-"* ]]; then
    var="$(realpath $var)"
  fi
  param+=($var)
done

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

python $SCRIPT_DIR/main.py ${param[*]}
