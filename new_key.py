from web3 import Web3
from web3.middleware import construct_sign_and_send_raw_middleware
import os
import time

ganache_url = 'http://0.0.0.0:57186'
w3 = Web3(Web3.HTTPProvider(ganache_url))

acct1 = w3.eth.accounts[0]

# Note: Never commit your key in your code! Use env variables instead:
pk = "48525704bd53cb8114b48c9dcff085910bf5d6546e16b161db5eb5009928a486"

# Instantiate an Account object from your key:
acct2 = w3.eth.account.from_key(pk)

for i in range(0, 100):
    time.sleep(3)
    
    # Add acct2 as auto-signer:
    w3.middleware_onion.add(construct_sign_and_send_raw_middleware(acct2))
    # pk also works: w3.middleware_onion.add(construct_sign_and_send_raw_middleware(pk))

    # Transactions from `acct2` will then be signed, under the hood, in the middleware:
    tx_hash = w3.eth.send_transaction({
        "from": acct2.address,
        "value": 0x9184e72a,
        "to": "0x878705ba3f8Bc32FCf7F4CAa1A35E72AF65CF766",
        "data": "0xabcd",
        "gasPrice": "0x9184e72a000",
        "gas": "0x76c0"
    })

    tx = w3.eth.get_transaction(tx_hash)
    print(tx_hash.hex())
    assert tx["from"] == acct2.address