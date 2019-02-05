from django.db import models

# Create your models here.
class SwpstkRule(models.Model):
    content = models.CharField(max_length=128,
                               help_text="rule description / 抽奖规则的描述，最多 128 个字节")

    def __str__(self):
        return self.content