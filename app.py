import requests

from config import SUBSCRIPTION_KEY, PATH, TRACE_ID

requestHeader = {
"Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY, 
"X-ClientTraceID": TRACE_ID 
}
req = requests.get(PATH, headers=requestHeader)

print(req);