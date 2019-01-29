from django.db.models import F

from ..models import Sweepstake

def get_all_values():
    """
    :return: 一个包含所有 Sweepstake 实例的字典
    """
    query_set = Sweepstake.objects.annotate(swpstkId=F('id'))
    res_dict = query_set.values("swpstkId", "swpstkName", "prizeName",
                                "prizeValue", "lotteryTime", "demoImage")
    res_dict = list(res_dict)
    return res_dict