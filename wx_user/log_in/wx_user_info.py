from ..models import WxUser
import json

def wx_user_info(openid, raw_data):
    raw_dict = json.loads(raw_data)
    raw_dict["openid"] = openid
    try:
        current_user = WxUser.objects.get(openid=openid)
        WxUser.objects.filter(openid=openid).update(**raw_dict)
    except WxUser.DoesNotExist:
        current_user = WxUser.objects.create(**raw_dict)
