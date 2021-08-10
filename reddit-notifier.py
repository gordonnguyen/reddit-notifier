import requests
import pandas as pd

auth = requests.auth.HTTPBasicAuth('oK3dTEYR7exUog', 'D2sVNa17qetOcmp35iA4LaPwec2Qkg')

data = {'grant_type': 'password',
    'username': 'GordonNguyen',
    'password': 'nhunhanss'}

headers = {'User-Agent': 'MyBot/0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

TOKEN = res.json()['access_token']

headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
print(headers)

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

res = requests.get("https://oauth.reddit.com/r/buildapcsales/new/",
headers=headers)

df = pd.DataFrame()

for post in res.json()['data']['children']:
    df = df.append({
        'subreddit': post['data']['subreddit'],
        'title': post['data']['title'],
        'selftext': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'score': post['data']['score']
    }, ignore_index=True)

print(df.head())
