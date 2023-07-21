import jwt
import time
import requests
import sys

ENGINE_API = "http://127.0.0.1:55109"

def request(payload_id):

    # Your 32-byte JWT secret key
    jwt_secret = bytes.fromhex("9d3359efbdb652f79a8c3c0e2e615e3cad253350bb67169ef9c25e5ae54cfe47")

    # Payload to be included in the JWT
    payload = {
        'iat': int(time.time())  # Add the 'iat' claim with the current timestamp
    }

    # Generate the JWT token
    token = jwt.encode(payload, jwt_secret, algorithm='HS256')

    # print("Generated JWT token:", token)

    payload = {"jsonrpc":"2.0", "method":"engine_getPayloadV2", "params": [payload_id], "id":1}

    print(f"trying payload id {payload_id}")
    response = requests.post(ENGINE_API, json = payload, headers = {"Content-type": "application/json", "Authorization": f"Bearer {token}"})

    print(response.json())


request(sys.argv[1])