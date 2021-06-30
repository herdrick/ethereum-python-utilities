#!/usr/bin/env python3

import click
from icecream import ic
import q
from web3 import Web3
import json
import sys

@click.command()
@click.argument('contract_address')
@click.argument('function_name')
@click.argument('abi_file', type=click.File('r'))
@click.option("--network", default="localhost", help="Ethereum network to use. If 'ropsten' or 'mainnet', use Infura, which requires the WEB3_INFURA_PROJECT_ID and WEB3_INFURA_API_SECRET env vars to be set. Default is 'localhost', ex. a local ganache node.")
@click.option("--transact/--call", default="False", help="""
If '--transact', initiate a transaction which will be executed on the blockchain.

If '--call', call a non-mutating 'view' function whose execution will only happen on the node you are connecting to).

Default is '--call'""")
@click.option('--ethereum_public_key', envvar='ETHEREUM_PUBLIC_KEY', help="Only used for --transact calls.")
@click.option('--ethereum_private_key', envvar='ETHEREUM_PRIVATE_KEY', help="Only used for --transact calls.")
@click.option("--nonce", type=int, default=None, help="Only used for --transact calls. If not set, w3.eth.getTransactionCount will be called and its result used as the nonce.")
def call_or_transact(contract_address, function_name, abi_file, network, transact, ethereum_public_key, ethereum_private_key, nonce):
    """Call a function of a smart contract. You must have either an Infura account, if the function is on the mainnet or ropsten, or you must be running a local node (ex. using ganache-cli).

    CONTRACT_ADDRESS: The address of the deployed contract.

    FUNCTION_NAME: Name of the function in the deployed contract. Ex. 'getCompletionStatusView'

    ABI_FILE: The ABI file of the deployed contract. (An ABI file is a JSON file specification of a contract.)

    """
    if transact:
        assert ethereum_public_key and ethereum_private_key, "If you specify --transact then you must specify ethereum_private_key and ethereum_public_key or set those env vars."
    if network == 'localhost':
        w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    if network == 'ropsten':
        from web3.auto.infura.ropsten import w3
    if network == 'mainchain':
        from web3.auto.infura.mainnet import w3
    ic(w3.api)
    ic(w3.eth.protocol_version)
    ic(w3)
    ic(w3.isConnected())
    assert w3.isConnected()
    abi = json.load(abi_file)
    contract_instance = w3.eth.contract(address=contract_address, abi=abi)
    ic(contract_instance.address)
    functions = contract_instance.all_functions()
    function = None
    for f in functions:
        if f.fn_name == function_name:
            function = f
    if not function:
        click.echo(f"Specified function {function_name} does not exist in contract {contract_address}")
        sys.exit(1)
    ic(function)
    if transact:
        ic(ethereum_public_key, ethereum_private_key)
        if not nonce:
            ic("no nonce specified; let's get it from w3.eth.getTransactionCount")
            nonce = w3.eth.getTransactionCount(ethereum_public_key)
        ic(nonce)
        #     w3.eth.send_raw_transaction(w3.eth.account.sign_transaction(f       ().buildTransaction({'nonce': account_tx_count}), private_key).rawTransaction)
        transaction_result = w3.eth.send_raw_transaction(w3.eth.account.sign_transaction(function().buildTransaction({'nonce': nonce}), ethereum_private_key).rawTransaction)
        ic(transaction_result)
        click.echo(f"Success? Transaction address: {transaction_result.hex()}")
    else:
        call_result = function().call()
        ic(type(call_result))
        ic(call_result)


if __name__ == "__main__":
    call_or_transact()
