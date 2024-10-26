#!/bin/bash

# echo "# ENTOPYSCALING" >> README.md
# git init
git add *
git commit -m "Chnages to Source of MC for reading alpha and rcut from the input files"
git branch -M main
git remote add origin https://github.com/Darz2/ENTOPYSCALING.git
git push -u origin main