from django.contrib import admin
from api.models import *


class UnifiedOrderAdmin(admin.ModelAdmin):
    list_display = ['out_trade_no', 'mch_id', 'body', 'appid',
                    'nonce_str', 'sign', 'total_fee', 'trade_type',
                    'openid', 'product_id', 'prepay_id']


admin.site.register(UnifiedOrder, UnifiedOrderAdmin)
