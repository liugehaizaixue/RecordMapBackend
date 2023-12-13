from database import Session
from werkzeug.exceptions import BadRequest
import requests
import json

MYAPPSECRET = "93092c143a39390356ffc13835c0de71"
MYAPPID = "wxc5edc973cc774d0d"

class UserService:
    
    def login(self,js_code):
        url = f"https://api.weixin.qq.com/sns/jscode2session?appid={MYAPPID}&secret={MYAPPSECRET}&js_code={js_code}&grant_type=authorization_code"
        try:
            response = requests.get(url)
            print(response.status_code)
            if response.status_code == 200:
                wx_user_data = json.loads(response.content.decode('utf-8'))
                if wx_user_data["openid"]:
                    return {'result': True,'data': {'openid': wx_user_data["openid"]}}
            return {'result': False,'data': {'error': 'Login Error'}}
        except Exception as e:
            print(e)
            return {'result': False,'data': {'error': 'Login Error'}}