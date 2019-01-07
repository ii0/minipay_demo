import json

from django.http import HttpResponse

import minipay


def query_mini_program_order(request, out_trade_no):
    query = minipay.OrderQuery(out_trade_no=out_trade_no)
    query.request()
    if query.is_success:
        print(query.response_data)
    else:
        print(query.error)
    return HttpResponse(json.dumps(query.response_data, ensure_ascii=False), content_type="application/json")
