from django.db.models import F

from ..models import Sweepstake
from lottery_backend.settings import DEBUG

def get_all_values():
    """
    :return: 一个包含所有 Sweepstake 实例的字典
    """
    query_set = Sweepstake.objects.annotate(swpstkId=F('id'))
    res_dict = query_set.values("swpstkId", "swpstkName", "prizeName",
                                "prizeValue", "lotteryTime", "demoImage")
    res_dict = list(res_dict)
    if DEBUG:
        print(res_dict)
    return res_dict