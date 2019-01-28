from django.db.utils import IntegrityError

from ..models import Participate

def check_exsist(wx_user, swpstk):
    try:
        Participate.objects.get(partWxUser=wx_user, partSwpstk=swpstk)
        return True
    except Participate.DoesNotExist:
        return False