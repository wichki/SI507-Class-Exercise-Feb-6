from requests_oauthlib import OAuth1Session
import secrets
import json

client_key = secrets.client_key
client_secret = secrets.client_secret

resource_owner_key = "959133679271497728-gTt0DvTOfJbvcNt5SgRhfzG4vHwBOZY"
resource_owner_secret = "mCm1IAE5QywukISh31DnBda2t58jRmSpw0a8tq7RvVwET"

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
tweets = json.loads(r.text)

in_it = tweets["statuses"]

for i in in_it:
    print("Username: " + i["user"]["screen_name"])
    print("Text: " + i["text"])
    print("\n")
