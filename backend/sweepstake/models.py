from django.db import models

# Create your models here.
class Prize(models.Model):
    prizeName = models.CharField(max_length=64, unique=True,
        help_text="Name of prize / 本次抽奖奖品的名称")
    prizeValue = models.IntegerField(
        help_text="Value of prize / 本次抽奖奖品的价值")
    demoImage = models.ImageField(upload_to='merchandise',
        help_text="A image demostrates the prize / 奖品描述的图片")

    def __str__(self):
        return self.prizeName


class PrizeGroup(models.Model):
    firstPrize = models.ForeignKey(Prize,
        on_delete=models.CASCADE,
        related_name="first",
        help_text="first prize / 一等奖（奖项需要预先建立）"
    )
    secondPrize = models.ForeignKey(Prize,
        on_delete=models.CASCADE,
        related_name="second",
        help_text="second prize / 二等奖（奖项需要预先建立）"
    )
    thirdPrize = models.ForeignKey(Prize,
        on_delete=models.CASCADE,
        related_name="third",
        help_text="third prize / 三等奖（奖项需要预先建立）"
    )
    luckyPrize = models.ForeignKey(Prize,
        on_delete=models.CASCADE,
        related_name="lucky",
        help_text="third prize / 幸运等奖（奖项需要预先建立）"
    )

    def __str__(self):
        return f"1({self.firstPrize.prizeName})==>" \
               f"2({self.secondPrize.prizeName})==>" \
               f"3({self.thirdPrize.prizeName})==>" \
               f"l({self.luckyPrize.prizeName})"


class Sweepstake(models.Model):
    swpstkName = models.CharField(max_length=64,
                help_text="Name of sweepstake / 本次抽奖的名称")
    lotteryTime = models.DateTimeField(
                help_text="Result date & time / 本次抽奖公布结果的时间")
    bindPrizes = models.OneToOneField(PrizeGroup,
                on_delete=models.SET_NULL, null=True,
                help_text="bind prize group of this sweepstake<br />本抽奖活动所绑定的奖励组")

    def __str__(self):
        return self.swpstkName

