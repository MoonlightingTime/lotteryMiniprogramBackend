from ..models import SwpstkRule

def all_rules():
    content_dic = SwpstkRule.objects.values("content")
    return [c['content'] for c in content_dic]