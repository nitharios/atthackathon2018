import requests

from config import SUBSCRIPTION_KEY, PATH, TOKEN_PATH, TRACE_ID

requestHeader = {
  "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY
}

params = {
  "from": "en-us",
  "to": "it-IT",
  "features": "texttospeech",
  "api-version": "1.0"
}

# token = requests.post(TOKEN_PATH, headers=requestHeader)
# token = str(token.content)[1:-1]
# token = str(token)

req = requests.get(PATH, headers=requestHeader, params=params)

print(req.content)
