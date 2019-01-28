from django.db import models

# Create your models here.
class WxUser(models.Model):
    openid = models.CharField(max_length=64, primary_key=True)
    nickName = models.CharField(max_length=64)
    gender = models.BooleanField(null=True)
    language = models.CharField(max_length=16)
    city = models.CharField(max_length=16)
    province = models.CharField(max_length=16)
    country = models.CharField(max_length=8)
    avatarUrl = models.URLField()

    phoneNumber = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return f"{self.nickName}({self.city}, {self.province})"
