from django.db import connection
from django.db.models import F

from ..models import Sweepstake

def get_all_values():
    """
    :return: 一个包含所有 Sweepstake 实例的字典
    """
    sql1 = \
        """
        SELECT prizeName, prizeValue, demoImage, t1.id
        FROM sweepstake_sweepstake t1
        INNER JOIN sweepstake_prizegroup t2 ON t1.bindPrizes_id=t2.id
        INNER JOIN sweepstake_prize t3 ON t2.
        """
    sql2 = "_id=t3.id WHERE t1.id="
    prizes_lst = ["firstPrize", "secondPrize", "thirdPrize", "luckyPrize"]

    query_set = Sweepstake.objects.annotate(swpstkId=F('id'))
    resdict_lst = list(query_set.values("swpstkId", "swpstkName", "lotteryTime"))

    for resdict in resdict_lst:
        for prize in prizes_lst:
            cursor = connection.cursor()
            cursor.execute(f"{sql1}{prize}{sql2}{resdict['swpstkId']};")
            row = cursor.fetchone()
            resdict[prize] = row and {
                "prizeName": row[0], "prizeValue": row[1], "demoImage": row[2]
            }
    return resdict_lst
