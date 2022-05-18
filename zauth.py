#!/usr/bin/env python3


import requests
import json
import time

tenant = "admin.zscalernode.net"

url = f"http://{tenant}/api/v1/authenticatedSession"
api_key = "XXXXX"

seed = api_key
now = int(time.time() * 1000)
n = str(now)[-6:]
r = str(int(n) >> 1).zfill(6)
key = ""
for i in range(0, len(str(n)), 1):
    key += seed[int(str(n)[i])]
for j in range(0, len(str(r)), 1):
    key += seed[int(str(r)[j]) + 2]

payload = json.dumps({
    "username": "username@domain.com",
    "password": r"Password_Key",
    "apiKey": key,
    "timestamp": now
})

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
}

response = requests.post(url, headers=headers, data=payload)
#print(response.text)
cookie = (response.headers['Set-Cookie'])
session_id = cookie[:cookie.index(';')]
#print(session_id)