#!/usr/bin/bash

if [[ $# -ne 1 ]]; then
    echo "pass day number"
    exit 1
fi

cd "$(dirname "$0")" || exit

day=$1
solutionsDir="solutions"
solutionFile="${solutionsDir}/solve${day}.py"
dayInputDirectory="input_puzzles/day${day}"

if [[ -f "${solutionFile}" ]]; then
  echo "solution file already exists, exiting ..."
  exit
fi

mkdir -p "${dayInputDirectory}"
if [[ $? -ne 0 ]]; then
  echo "failed to create input directory, exiting ..."
  exit
fi


cp ${solutionsDir}/solveTemplate.py "${solutionFile}"
sed -i "s/DAY_NUM/${day}/g" "${solutionFile}"

touch "${dayInputDirectory}/example"

wget --no-cookies --header "Cookie: $(cat session.cookie)" https://adventofcode.com/2024/day/10/input
mv input "${dayInputDirectory}/input"

echo "Day ${day} initialized."
