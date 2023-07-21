import requests
import time
START_NOCE = 200291

def send_transaction(nonce):

    rpc_endpoint = "http://0.0.0.0:57186"
    data = {"method":"eth_sendTransaction","params":[{"from": "0x4E9A3d9D1cd2A2b2371b8b3F489aE72259886f1A","to": "0x878705ba3f8Bc32FCf7F4CAa1A35E72AF65CF766","gas": "0x76c0","gasPrice": "0x9184e72a000","value": "0x9184e72a","data": "0xabcd"}],"id":1,"jsonrpc":"2.0"}
    response = requests.post(rpc_endpoint, json=data, headers={"Content-type": "application/json"})
    if response.status_code == 200:
        txJson = response.json()
        tx = txJson["result"]
        print(f"sent transaction with hash {tx}; waiting for status")
        # while True:
        #     data = {"method":"eth_getTransactionReceipt", "params": [tx],"id":1,"jsonrpc":"2.0"}
        #     response = requests.post(rpc_endpoint, json = data, headers={"Content-type": "application/json"})
        #     time.sleep(5)
        #     if response.status_code == 200 and response.json()['result'] == None:
        #         continue
        #     elif response.status_code == 200:
        #         rxJson = response.json()
        #         status = rxJson["result"]["status"]
        #         if status == "0x1":
        #             print(f"tx {tx} succeeded")
        #         else:
        #             print(f"tx {tx} failed")
        #         break
        #     elif response.status_code != 200:
        #         print("this shouldn't happen")
        #         break
            

for nonce in range(START_NOCE, START_NOCE + 50000):
    send_transaction(nonce)
    time.sleep(0.3)
