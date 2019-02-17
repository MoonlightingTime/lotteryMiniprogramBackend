from ..models import Participate

def query_all_swpstk(wx_user):
    ppates = Participate.objects.filter(partWxUser=wx_user)
    res_dic = [{
        "swpstkId": p.partSwpstk.id,
        "swpstkName": p.partSwpstk.swpstkName,
        "swpstkState": p.lotteryResult,
        "specificResult": p.specificResult,
    } for p in ppates]
    return res_dic
