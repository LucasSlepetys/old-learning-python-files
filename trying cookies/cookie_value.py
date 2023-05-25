import requests
import json

session = requests.Session()
session.headers.update({'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320"})
mydata = json.dumps({'login': '','password': ''})
response = session.post('https://fis.learning.powerschool.com/do/account/login',data=mydata)
session.get('https://fis.learning.powerschool.com/u/roberto./portal')
session.post('https://fis.learning.powerschool.com/u/roberto./portal')

print(response.text)

# with open('cookies.json', 'w') as f:
#     json.dump(requests.utils.dict_from_cookiejar(session.cookies), f)
# with open('cookies.json', 'r') as f:
#     session.cookies = requests.utils.cookiejar_from_dict(json.load(f))
#     print(session.cookies['_session_id'])