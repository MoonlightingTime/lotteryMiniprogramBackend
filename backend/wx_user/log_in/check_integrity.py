import hashlib
from lottery_backend.settings import DEBUG

def check_integrity(raw_data, session_key, signature):
    """
    根据腾讯小程序 API 提供的算法检验完整性：
    - https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/signature.html
    :param raw_data: 前端传输的原始数据
    :param senssion_key: code2session 返回的数据
    :param signature: 前端传输的签名
    :return:
    """
    if DEBUG:
        print(raw_data, session_key, signature)
    plain_text = (raw_data + session_key).encode()
    sha = hashlib.sha1(plain_text)
    mySignature = sha.hexdigest()
    return True if mySignature==signature else False