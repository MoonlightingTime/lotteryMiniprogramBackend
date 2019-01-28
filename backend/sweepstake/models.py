from django.db import models

# Create your models here.
class Sweepstake(models.Model):
    swpstkName = models.CharField(max_length=64,
                help_text="Name of sweepstake / 本次抽奖的名称")
    prizeName = models.CharField(max_length=64,
                help_text="Name of prize / 本次抽奖奖品的名称")
    prizeValue = models.IntegerField(
                help_text="Value of prize / 本次抽奖奖品的价值")
    lotteryTime = models.DateTimeField(
                help_text="Result date & time / 本次抽奖公布结果的时间")
    demoImage = models.ImageField(upload_to='merchandise',
                help_text="A image demostrates the prize / 奖品描述的图片")

    def __str__(self):
        return self.swpstkName

