import requests
import json as JSON
url = "https://slate.host/api/v3/get"
headers = {
    "content-type": "application/json",
    "Authorization": "<auth-key>"  # <authorization-key>
}
r = requests.get(url, headers=headers)
print(JSON.dumps(r.json(), indent=2))
