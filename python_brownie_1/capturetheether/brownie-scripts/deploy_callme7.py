#!/usr/bin/python3

#  MUST BE RUN LIKE SO:   $ brownie run scripts/deploy_callme7.py

from brownie import accounts, config, network
from brownie import CallMe7

# USAGE:
#  brownie run scripts/deploy_callme7.py



# mainnet_eth_usd_address = '0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419'
# kovan_eth_usd_address = '0x9326BFA02ADD2366b30bacB125260Af641031331'

def main():
    # accounts.load('0')
    callme7_deployed = CallMe7.deploy( {"from": accounts[0]} )
    print( "ok, I deployed my contract in transaction: ", callme7_deployed.tx)
