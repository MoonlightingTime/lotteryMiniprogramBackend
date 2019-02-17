from django.db import models

# import developer code
from wx_user.models import WxUser
from sweepstake.models import Sweepstake

# Create your models here.
class Participate(models.Model):
    partWxUser = models.ForeignKey(WxUser, on_delete=models.CASCADE,
           help_text="Participator / 参与抽奖的用户.")
    partSwpstk = models.ForeignKey(Sweepstake, on_delete=models.CASCADE,
           help_text="Participate target / 参与的抽奖的目标.")
    lotteryResult = models.BooleanField(null=True,
            help_text="`Unkown` stands for notTime / `Unkown` 表示尚未知晓结果;<br />"
                      "`Yes` stands for having won lottery / `Yes` 表示已经中奖;<br />"
                      "`No` stands for having not won lottery. / `No` 表示没有中奖")

    resultChoice = (
        (0, "firstPrize"), (1, "secondPrize"),
        (2, "thirdPrize"), (3, "luckyPrize")
    )
    specificResult =models.IntegerField(
        null=True, blank=True, choices=resultChoice)

    class Meta:
        """
        partWxUser&partSweepstake is a union key
        """
        unique_together = ["partWxUser", "partSwpstk"]

    def __str__(self):
        return f"{str(self.partWxUser)}=>{self.partSwpstk.swpstkName}"