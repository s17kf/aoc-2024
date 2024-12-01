#!/usr/bin/bash

if [[ $# -ne 1 ]]; then
    echo "pass day number"
    exit 1
fi

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

touch "${dayInputDirectory}/exampleData.txt"

echo "Day ${day} initialized."
