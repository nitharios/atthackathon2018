import requests

from config import SUBSCRIPTION_KEY, TOKEN_PATH, TRACE_ID

requestHeader = {
  "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY
}

token = requests.post(TOKEN_PATH, headers=requestHeader)

# req = requests.get(PATH, headers=requestHeader)

print(token.content)
