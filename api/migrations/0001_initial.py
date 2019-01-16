# Generated by Django 2.1.5 on 2019-01-16 11:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UnifiedOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appid', models.CharField(max_length=18, verbose_name='AppID')),
                ('mch_id', models.CharField(max_length=10, verbose_name='商户号')),
                ('nonce_str', models.CharField(blank=True, max_length=32, verbose_name='随机字符串')),
                ('sign', models.CharField(blank=True, max_length=32, verbose_name='签名')),
                ('body', models.CharField(blank=True, max_length=128, null=True, verbose_name='商品描述')),
                ('out_trade_no', models.CharField(max_length=32, verbose_name='商户订单号')),
                ('total_fee', models.IntegerField(blank=True, verbose_name='标价金额')),
                ('spbill_create_ip', models.CharField(default='47.94.162.104', max_length=16, verbose_name='终端ip')),
                ('notify_url', models.CharField(max_length=255, verbose_name='通知回调地址')),
                ('trade_type', models.CharField(default='JSAPI', max_length=16, verbose_name='交易类型')),
                ('openid', models.CharField(blank=True, max_length=32, null=True, verbose_name='openid')),
                ('result_code', models.CharField(blank=True, max_length=16, verbose_name='业务结果')),
                ('result_msg', models.CharField(blank=True, max_length=128, verbose_name='返回信息')),
                ('err_code', models.CharField(blank=True, max_length=32, verbose_name='错误代码')),
                ('return_code', models.CharField(blank=True, max_length=32, verbose_name='返回状态')),
                ('err_code_des', models.CharField(blank=True, max_length=128, verbose_name='错误代码描述')),
                ('prepay_id', models.CharField(blank=True, max_length=64, verbose_name='预支付交易会话标识')),
                ('code_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='二维码链接')),
                ('product_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='商品id')),
                ('add_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '统一下单',
                'verbose_name_plural': '统一下单',
                'db_table': 'unified_order',
            },
        ),
    ]
