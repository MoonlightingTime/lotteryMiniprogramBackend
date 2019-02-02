from django.contrib import admin

# Register your models here.
from .models import Sweepstake, Prize, PrizeGroup
# from .models import Prize

admin.site.register(Sweepstake)
admin.site.register(Prize)
admin.site.register(PrizeGroup)