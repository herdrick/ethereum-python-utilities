#!/usr/bin/env python
# Example usage:
# export WEB3_INFURA_API_SECRET=ed8f200d918a4dfda1b570148962e19b
# export WEB3_INFURA_PROJECT_ID=a4ba36cd7a394f3b900f09dc9a03b65f



from icecream import ic
import os

def transact(w3, f):
    private_key = os.environ['ETHEREUM_PRIVATE_KEY']
    account_tx_count = w3.eth.getTransactionCount(os.environ['ETHEREUM_PUBLIC_KEY'])
    ic(account_tx_count)
    ic('sending signed transaction to ', w3)
    transaction_result = w3.eth.send_raw_transaction(w3.eth.account.sign_transaction(f().buildTransaction({'nonce': account_tx_count}), private_key).rawTransaction)
    ic(transaction_result)
    return transaction_result



if __name__ == "__main__":
    print ("starting ", __name__)
    from web3.auto.infura.ropsten import w3 as w3_ropsten
    ic(w3_ropsten.api)
    ic(w3_ropsten.eth.protocol_version)
    abi = [
    {
        "inputs": [],
        "name": "_isComplete",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getCompletionStatusPublic",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getCompletionStatusView",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "markComplete",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "markNotComplete",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
    ]
    ic('getting contract from chain...')
    contract_instance = w3_ropsten.eth.contract(address='0xfE7740E72ADD4a6b22c5a53e4E4ac71fFe19EF34', abi=abi)
    ic(contract_instance.all_functions())
    ic('calling functions:')
    ic(contract_instance.functions.getCompletionStatusView().call())

    #ic(transact(w3_ropsten, contract_instance.functions.markComplete))
    #ic(contract_instance.functions.getCompletionStatusView().call())

    ic(transact(w3_ropsten, contract_instance.functions.markNotComplete))
    ic(contract_instance.functions.getCompletionStatusView().call())
