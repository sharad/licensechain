
from eth_account import Account
import os

WALLET_FILE = "wallet.key"

def get_wallet():
    if os.path.exists(WALLET_FILE):
        with open(WALLET_FILE, "r") as f:
            key = f.read().strip()
            acct = Account.from_key(key)
            return acct
    else:
        acct = Account.create()
        with open(WALLET_FILE, "w") as f:
            f.write(acct.key.hex())
        return acct
