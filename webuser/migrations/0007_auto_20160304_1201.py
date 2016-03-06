# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0006_auto_20160304_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenthremploy',
            name='master',
            field=models.CharField(blank=True, max_length=10, verbose_name='\u4e3b\u52a8\u65b9', choices=[('\u5b66\u751f', '\u5b66\u751f'), ('HR', 'HR')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studenthremploy',
            name='status',
            field=models.CharField(default='\u672a\u7b54\u590d', max_length=10, verbose_name='\u72b6\u6001', choices=[('\u540c\u610f', '\u540c\u610f'), ('\u62d2\u7edd', '\u62d2\u7edd'), ('\u672a\u7b54\u590d', '\u672a\u7b54\u590d')]),
            preserve_default=True,
        ),
    ]
