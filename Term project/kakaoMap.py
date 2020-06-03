import requests
import json
import http.client

url = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.xml"
headers = {"Authorization": "KakaoAK c11cd41a6b4ce614ae81b1b07cc954eb"}

api_test = requests.get(url,headers=headers)
url_text = json.loads(api_test.text)


print(url_text)