import requests

# TODO: Verify with username & mirrorID?
# TODO: Verify using a query or passing parameters?

r = requests.get("http://localhost:3000/api/get_user_settings?username=test&mirrorID=test")
r.json();
print r.text;
