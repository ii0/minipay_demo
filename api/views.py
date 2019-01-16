import json

from django.http import HttpResponse

import minipay
from api.models import UnifiedOrder


def query_mini_program_order(request, out_trade_no):
    query = minipay.OrderQuery(out_trade_no=out_trade_no)
    query.request()
    print(query.config)

    if query.is_success:
        print(query.response_data)
    else:
        print(query.error)
    return HttpResponse(json.dumps(query.response_data, ensure_ascii=False), content_type="application/json")


def unified_mini_program_order(request, out_trade_no):
    unified = minipay.UnifiedOrder(
        out_trade_no=out_trade_no, body="body", total_fee=100, openid="123123", model=UnifiedOrder, mode="store")
    unified.request()
    print(unified.config)

    if unified.is_success:
        print(unified.response_data)
    else:
        print(unified.error)
    return HttpResponse(json.dumps(unified.response_data, ensure_ascii=False), content_type="application/json")
