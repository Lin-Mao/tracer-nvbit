#! /bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <script_name>"
    exit 1
fi

LD_PRELOAD=../tracer_tool/tracer_tool.so python $1
