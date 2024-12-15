#!/bin/sh

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <year> <day>"
    exit 1
fi

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/$1/day"$(printf "%02d" "$2")
URL="https://adventofcode.com/$1/day/$2"

mkdir -p $DIR
curl -H "Cookie: session=$AOC_SESSION" $URL"/input" -o $DIR/input.txt

echo "cd $DIR"
echo $URL
