#!/usr/bin/bash

if [[ $# -ne 2 ]]; then
    echo "pass input file name and day number"
    exit 1
fi

cd "$(dirname "$0")" || exit

day=$2
input_file=$1

./solutions/solve"${day}".py input_puzzles/day"${day}"/"${input_file}"
