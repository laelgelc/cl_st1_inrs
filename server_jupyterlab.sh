#!/bin/bash

nohup jupyter-lab --ip 0.0.0.0 --no-browser --allow-root &
jupyter server list
