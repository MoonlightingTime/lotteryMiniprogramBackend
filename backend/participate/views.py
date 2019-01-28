
from lottery_backend.pubfuc import JsonResponseZh

# Create your views here.
from .participate_in.get_model import get_wx_user, get_swpstk
from .participate_in.participate_sweepstake import participate_sweepstake
def check_participated(request):
    openid = request.GET.get("openid")
    swpstk_id = request.GET.get("swpstkId")

    if (openid is None) or (swpstk_id is None):
        # TODO: 如果请求参数中不含有 openid 或 swpstkId，请求参数不合法
        return JsonResponseZh({
            "code": "400",
            "msg": "Bad Request."
        })
    wx_user, swpstk = get_wx_user(openid), get_swpstk(swpstk_id)
    if (wx_user is None) or (swpstk_id is None):
        # TODO: 如果得到结果为 None，则参数内容不正确
        return JsonResponseZh({
            "code": 422,
            "msg": "Unprocessable Entity"
        })
    if check_exsist(wx_user, swpstk):
        # TODO: 检查该用户是否已经参与过此次抽奖
        return JsonResponseZh({
            "code": 1,
            "msg": "你已经参与过此次抽奖了"
        })
    return JsonResponseZh({
        "code": 0,
        "msg": "可以参与此次抽奖",
        "data": {"phoneNumber": wx_user.phoneNumber}
    })

from .check_participated.check_exsist import check_exsist
def participate_in(request):
    openid = request.GET.get("openid")
    swpstk_id = request.GET.get("swpstkId")
    phone_number = request.GET.get("phoneNumber")
    if (openid is None) or (swpstk_id is None) or (phone_number is None):
        # TODO: 如果请求参数中不含有 openid 或 swpstkId，请求参数不合法
        return JsonResponseZh({
            "code": "400",
            "msg": "Bad Request."
        })
    wx_user, swpstk = get_wx_user(openid), get_swpstk(swpstk_id)
    if (wx_user is None) or (swpstk_id is None):
        # TODO: 如果得到结果为 None，则参数内容不正确
        return JsonResponseZh({
            "code": 422,
            "msg": "Unprocessable Entity"
        })
    if not participate_sweepstake(wx_user=wx_user, swpstk=swpstk, phone_number=phone_number):
        # TODO: 如果返回 False，说明该参与对象已经存在
        return JsonResponseZh({
            "code": 1,
            "msg": "你已经参与过此次抽奖了"
        })
    return JsonResponseZh({
        "code": 0,
        "msg": "参与成功"
    })

from .query_participate.query_all_swpstk import query_all_swpstk
def query_participated(request):
    openid = request.GET.get("openid")
    if openid is None:
        # TODO: 如果请求参数中不含有 openid，请求参数不合法
        return JsonResponseZh({
            "code": "400",
            "msg": "Bad Request."
        })
    wx_user = get_wx_user(openid)
    if wx_user is None:
        # TODO: 如果得到结果为 None，则参数内容不正确
        return JsonResponseZh({
            "code": 422,
            "msg": "Unprocessable Entity"
        })
    all_participated = query_all_swpstk(wx_user)
    return JsonResponseZh({
        "code": 0,
        "msg": "查询参与情况成功",
        "data": all_participated,
    })