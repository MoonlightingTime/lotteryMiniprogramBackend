from ..models import Participate

def query_all_swpstk(wx_user):
    ppates = Participate.objects.filter(partWxUser=wx_user)
    res_dic = [{
        "swpstkName": p.partSwpstk.swpstkName,
        "swpstkState": p.lotteryResult,
        "swpstkId": p.partSwpstk.id,
    } for p in ppates]
    return res_dic
