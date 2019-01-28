from django.shortcuts import render

from lottery_backend.pubfuc import JsonResponseZh
from .log_in.code2session import code2session
from .log_in.wx_user_info import wx_user_info
from .log_in.check_integrity import check_integrity

# Create your views here.
def log_in(requests):
    code = requests.GET.get("code")
    raw_data = requests.GET.get("rawData")
    signature = requests.GET.get("signature")

    if (code is None) or (raw_data is None) or (signature is None):
        # TODO: GET 请求没有 code 或 alias 或 signature 参数，请求不合法
        return JsonResponseZh({
            "code": 400,
            "msg": "Bad Request."
        })
    status, jsondic = code2session(code)
    if status != 200:
        # TODO: 网络状态不是 200，网络请求出现问题
        return JsonResponseZh({
            "code": status,
            "msg": "code2session api request fail."
        })
    openid = jsondic.get("openid", None)
    if openid is None:
        # TODO: 返回数据包中没有 openid 参数，请求失败
        return JsonResponseZh({
            "code": jsondic.get("errcode", 404),
            "msg": jsondic.get("errmsg", "Error message not found")
        })
    if not check_integrity(raw_data, jsondic["session_key"], signature):
        # TODO: 使用 raw_data, session_key 和 signature 检查完整性，如果检查完整性失败返回 403
        return JsonResponseZh({
            "code": 403,
            "msg": "Forbidden. Check integrity failed."
        })
    # TODO: 如果 openid 不在数据库中，加入数据库；否则更新其 alias
    wx_user_info(openid, raw_data)
    return JsonResponseZh({
        "code": 0,
        "msg": "请求成功",
        "data": {"openid": openid},
    })

