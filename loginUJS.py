import requests
from bs4 import BeautifulSoup
import muggle_ocr
import base64
from Crypto.Cipher import AES


class aesEncrypt:
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv

    def pad(self, data):
        # https://stackoverflow.com/questions/14179784/python-encrypting-with-pycrypto-aes
        data = bytes(data, encoding="utf-8")
        length = 16 - (len(data) % 16)
        data += bytes([length]) * length
        return data

    def encrypt(self, rawData):
        data = self.pad(rawData)
        chip = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(chip.encrypt(data))


class Login:
    addition = 'eJFAF3ZnD4sKpFKhA3rNbnht6nZPKXKeMxKR5e7MhkCwBZEwwfZXszf25APPp6Fn'
    iv = 'aNjp4cpa7SH8tSG5'


headers = {
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://yun.ujs.edu.cn',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0',
        'Accept': 'text/html',
        'Referer': 'http://yun.ujs.edu.cn/xxhgl/yqsb/grmrsb',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
    }


def get_cookie(username, password):
    s = requests.Session()
    response = s.get('https://pass.ujs.edu.cn/cas/login', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    key = soup.find(id='pwdDefaultEncryptSalt')['value']
    lt = soup.find('input', {'name': 'lt'})['value']
    execution = soup.find('input', {'name': 'execution'})['value']
    enc = aesEncrypt(bytes(key, encoding='utf-8'), bytes(Login.iv, encoding='utf-8'))
    addition = Login.addition
    password = str(enc.encrypt(addition + password), encoding='utf-8')
    # 识别验证码
    captcha_bytes = s.get('https://pass.ujs.edu.cn/cas/captcha.html', headers=headers).content
    sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
    captha = sdk.predict(image_bytes=captcha_bytes)
    # 登录
    data = {
        'username': username,
        'password': password,
        'lt': lt,
        'dllt': 'userNamePasswordLogin',
        'execution': execution,
        '_eventId': 'submit',
        'rmShown': '1',
        'captchaResponse': captha
    }
    s.post('https://pass.ujs.edu.cn/cas/login', headers=headers, data=data)
    s.get('http://yun.ujs.edu.cn/site/login', headers=headers)
    s.get('http://yun.ujs.edu.cn/xxhgl/yqsb/index', headers=headers, allow_redirects=False)
    return s.cookies['cloud_sessionID']
