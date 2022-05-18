#!/usr/bin/python3

import http.client
import json
import argparse
from zauth import session_id, tenant

conn = http.client.HTTPSConnection(tenant)

parser = argparse.ArgumentParser(description="Checking of URL Category in ZIA.")
parser.add_argument('--url', '-u', help="Domains to be checked.", type=str, nargs="*")
parser.add_argument('--file', '-f', metavar='', help="Path to the Text File to be lookup")
args = parser.parse_args()

targetURL = args.url
targetFILE = args.file
if targetURL:
  payload = json.dumps(
    targetURL
  )
  
elif targetFILE:
  files = open(targetFILE, "r")
  f = files.readlines()
  urls = []
  for url in f:
    url = url.strip("\n")
    urls.append(url)
  
  payload = json.dumps(
    urls
  )


headers = {
  'Content-Type': 'application/json',
  'cookie': session_id
}

conn.request("POST", "/api/v1/urlLookup", payload, headers)
res = conn.getresponse()
data = json.loads(res.read())

for item in data:
    url = item['url']
    cats = item['urlClassifications']
    cat = ' '.join(cats)
    alert = item['urlClassificationsWithSecurityAlert']
    if alert == []:
      alert = False
    print(f"URL: {url}, Category: {cat}, Security Alert: {alert}")

