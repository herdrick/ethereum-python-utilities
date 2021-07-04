#!/usr/bin/python3

# USAGE:
#  MUST BE RUN with 'brownie run'

import json
import os
import sys

def main():
    classname = os.environ['SOLIDITY_CLASS']
    #print(f"classname: {classname}", file=sys.stderr)
    mod = __import__('brownie', fromlist=[classname])
    print(json.dumps(getattr(mod, classname).abi))
