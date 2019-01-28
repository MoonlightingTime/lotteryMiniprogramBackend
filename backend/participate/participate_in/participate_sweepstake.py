from django.db.utils import IntegrityError

from ..models import Participate

def participate_sweepstake(wx_user, swpstk, phone_number):
    wx_user.phoneNumber = phone_number
    wx_user.save()
    try:
        Participate.objects.create(partWxUser=wx_user, partSwpstk=swpstk)
        return True
    except IntegrityError:
        return False