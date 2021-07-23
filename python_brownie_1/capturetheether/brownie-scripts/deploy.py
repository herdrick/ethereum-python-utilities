#!/usr/bin/python3

# USAGE:
#    export SOLIDITY_CLASS=TypesDemo && brownie run scripts/deploy.py

from brownie import accounts, config, network
import os
from icecream import ic

def main():
    classname = os.environ['SOLIDITY_CLASS']
    print('deploying', classname)
    #print(f"classname: {classname}", file=sys.stderr)
    module = __import__('brownie', fromlist=[classname])
    #print(module)
    klass = getattr(module, classname)
    #print('klass', klass)
    #print('type(klass)', type(klass))
    klass.deploy({"from": accounts[0]})
