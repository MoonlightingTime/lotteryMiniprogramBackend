from django.contrib import admin

# Register your models here.
from .models import WxUser
from lottery_backend.settings import DEBUG

if DEBUG:
    admin.site.register(WxUser)