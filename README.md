# Interacting with deployed contracts with Python

This is a convenience script useful for interacting with deployed contracts.

## Installation
Uses python 3.

```pip install -r web3-scripts/requirements.txt```

##
```
$ web3-scripts/invoke_function.py --help

Usage: invoke_function.py [OPTIONS] CONTRACT_ADDRESS FUNCTION_NAME ABI_FILE
                          [ARGS]...

  Call a function of a smart contract. You must have either an Infura account,
  if the function is on the mainnet or ropsten, or you must be running a local
  node (ex. using ganache-cli).

  CONTRACT_ADDRESS: The address of the deployed contract.

  FUNCTION_NAME: Name of the function in the deployed contract. Ex.
  'getStatus'

  ABI_FILE: A file containing the ABI of the deployed contract, in json
  format. If Brownie compiled the contract, you can look in the
  build/contracts directory for the json file for the contract's class, for
  example MyContract.json. That file's 'abi' field contains the json which
  should go in the ABI_FILE.

  Alternatively, you can get the abi json in the brownie console, and write it
  to a file, like so:

      import json
      from brownie import MyContract
      json.dumps(MyContract.abi)
      with open("abis/MyContract.abi.json", "w") as abi_file:
          abi_file.write(json.dumps(MyContract.abi))

Options:
  -v, --verbose                Write verbose logging to stderr.
  --network TEXT               Ethereum network to use. If 'ropsten',
                               'rinkeby', or 'mainnet', use Infura, which
                               requires the WEB3_INFURA_PROJECT_ID and
                               WEB3_INFURA_API_SECRET env vars to be set.
                               Default is 'localhost', which will connect to
                               http://127.0.0.1:8545 i.e. a local ganache
                               node.
  --transact / --call          If '--transact', initiate a transaction which
                               will be executed on the blockchain.

                               If '--call', call a non-mutating 'view'
                               function whose execution will only happen on
                               the node you are connecting to).

                               Default is '--call'
  --ethereum_public_key TEXT   Only used for --transact calls.
  --ethereum_private_key TEXT  Only used for --transact calls.
  --nonce INTEGER              Only used for --transact calls. If not set,
                               w3.eth.getTransactionCount will be called and
                               its result used as the nonce.
  --help                       Show this message and exit.


Example usage:

    python3 scripts/invoke_function.py 0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87 myFunction abis/MyContract.abi.json False
```
