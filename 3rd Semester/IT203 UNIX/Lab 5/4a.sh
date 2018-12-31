#!/bin/bash


sed -i -e '1 i <HTML>' input.txt
sed -i -e '$ a </HTML>' input.txt
cat input.txt
