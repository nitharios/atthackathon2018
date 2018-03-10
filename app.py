import requests
from urllib import request

from config import SUBSCRIPTION_KEY, PATH, TOKEN_PATH, TRACE_ID

requestHeader = {
"Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY
# "X-ClientTraceID": TRACE_ID 
}

token = request.urlopen(TOKEN_PATH, data=requestHeader)

# req = requests.get(PATH, headers=requestHeader)

print(token.read().decode('utf-8').get_content_charset());