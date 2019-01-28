
from lottery_backend.pubfuc import JsonResponseZh
from .query_swpstk.get_all_values import get_all_values

# Create your views here.
def query_swpstk(request):
    res_dict = get_all_values()
    return JsonResponseZh({
        "code": 0,
        "msg": "请求成功",
        "data": res_dict
    }, safe=False)