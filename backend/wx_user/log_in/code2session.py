import requests
from lottery_backend.secret import APP_ID, APP_SECRET
from lottery_backend.settings import DEBUG

def code2session(code):
    requests_url = "https://api.weixin.qq.com/sns/jscode2session"
    requests_data = {
        "appid": APP_ID,
        "secret": APP_SECRET,
        "js_code": code,
        "grant_type": "authorization_code"
    }
    # TODO：向腾讯 API 请求 session 和 openid
    response = requests.get(requests_url, params=requests_data)
    if DEBUG:
        print(response.text)
    return response.status_code, response.json()
