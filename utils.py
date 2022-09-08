import requests
import json
import schedule
import time
import logging

def score_user(msisdn, national_id):
  headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer 54763|E2jmjRM7xGmfhuWdUk2pO4SyHeDauvVer9sdCzGe'
  }
  payload = json.dumps({
  "national_id": f"{national_id}",
  "msisdn": f"{msisdn}",
  "amount": "1500"
  })
  url = "https://preprod.senti.co.ke/api/v5/scoring/query"
  r = requests.post(url, headers=headers,data=payload)
  print(f"Request: {payload} Response: {r.text}")
  return r.text