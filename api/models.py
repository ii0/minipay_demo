import datetime

from django.db import models


class UnifiedOrder(models.Model):
    appid = models.CharField(max_length=18, verbose_name='AppID')
    mch_id = models.CharField(max_length=10, verbose_name='商户号')
    nonce_str = models.CharField(max_length=32, verbose_name='随机字符串', blank=True)
    sign = models.CharField(max_length=32, verbose_name='签名', blank=True)
    body = models.CharField(max_length=128, verbose_name='商品描述', null=True, blank=True)
    out_trade_no = models.CharField(max_length=32, verbose_name='商户订单号')
    total_fee = models.IntegerField(verbose_name='标价金额', blank=True)
    spbill_create_ip = models.CharField(max_length=16, verbose_name='终端ip', default='47.94.162.104')
    notify_url = models.CharField(max_length=255, verbose_name='通知回调地址')
    trade_type = models.CharField(max_length=16, verbose_name='交易类型', default='JSAPI')
    openid = models.CharField(max_length=32, blank=True, verbose_name='openid', null=True)
    result_code = models.CharField(max_length=16, verbose_name='业务结果', blank=True)
    result_msg = models.CharField(max_length=128, verbose_name='返回信息', blank=True)
    err_code = models.CharField(max_length=32, verbose_name='错误代码', blank=True)
    return_code = models.CharField('返回状态', max_length=32, blank=True)
    err_code_des = models.CharField(max_length=128, verbose_name='错误代码描述', blank=True)
    prepay_id = models.CharField(max_length=64, verbose_name='预支付交易会话标识', blank=True)
    code_url = models.CharField(max_length=255, verbose_name='二维码链接', blank=True, null=True)
    product_id = models.CharField(max_length=255, verbose_name="商品id", blank=True, null=True)
    add_time = models.DateTimeField('添加时间', null=True, blank=True, default=datetime.datetime.now)

    class Meta:
        db_table = 'unified_order'
        verbose_name = '统一下单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.out_trade_no)

    @property
    def is_expired(self):
        now = datetime.datetime.now()
        if (now - self.add_time).total_seconds() > 7200:
            return True
        return False
