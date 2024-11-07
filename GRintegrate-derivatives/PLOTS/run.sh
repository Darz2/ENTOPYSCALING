#!/bin/bash

chi=(2 10 20)

for i in "${chi[@]}"
do

    python3 ${i}_gr.py
    python3 ${i}_ggr.py

done
