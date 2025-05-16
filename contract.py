from web3 import Web3
import json

# Connect to local blockchain (e.g., Ganache or Hardhat)
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Replace with your actual deployed contract address
contract_address = "0xYourContractAddressHere"

# Load contract ABI from a file (exported from Remix or Hardhat)
with open("LicenseChainABI.json") as f:
    abi = json.load(f)

contract = w3.eth.contract(address=contract_address, abi=abi)

def register_build_on_chain(resource_id, price_wei, from_address, private_key):
    tx = contract.functions.mint(resource_id, price_wei).build_transaction({
        'from': from_address,
        'value': price_wei,
        'nonce': w3.eth.get_transaction_count(from_address),
        'gas': 2000000,
        'gasPrice': w3.to_wei('20', 'gwei')
    })
    signed = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    print(f"Mint TX sent: {tx_hash.hex()}")
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Mint confirmed" if receipt.status == 1 else "Mint failed")

def transfer_license(resource_id, to_address, price, from_address, private_key):
    tx = contract.functions.sell(resource_id, to_address, price).build_transaction({
        'from': from_address,
        'nonce': w3.eth.get_transaction_count(from_address),
        'gas': 2000000,
        'gasPrice': w3.to_wei('20', 'gwei')
    })
    signed = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    print(f"Transfer TX sent: {tx_hash.hex()}")
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transfer confirmed" if receipt.status == 1 else "Transfer failed")

def get_owners(resource_id):
    return contract.functions.getOwners(resource_id).call()
