from wx_user.models import WxUser
from sweepstake.models import Sweepstake

def get_wx_user(openid):
    try:
        wx_user = WxUser.objects.get(openid=openid)
        return wx_user
    except WxUser.DoesNotExist:
        return None

def get_swpstk(swpstkId):
    try:
        swpstk = Sweepstake.objects.get(id=swpstkId)
        return swpstk
    except Sweepstake.DoesNotExist:
        return None