from django.shortcuts import render
from lottery_backend.pubfuc import JsonResponseZh

# Create your views here.
from .query_rules.all_rules import all_rules
def query_rules(request):
    content_lst = all_rules()
    return JsonResponseZh({
        "code": 0,
        "msg": "请求成功",
        "data": content_lst
    })