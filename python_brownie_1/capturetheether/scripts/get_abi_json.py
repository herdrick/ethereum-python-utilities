#!/usr/bin/python3

# MUST be run with 'brownie run'
# Example usage:
#  export SOLIDITY_CLASS=CallMe7; brownie run scripts/get_abi_json.py > abis/CallMe7.json

import json
import os
import sys

def main():
    classname = os.environ['SOLIDITY_CLASS']
    #print(f"classname: {classname}", file=sys.stderr)
    mod = __import__('brownie', fromlist=[classname])
    print(json.dumps(getattr(mod, classname).abi))
