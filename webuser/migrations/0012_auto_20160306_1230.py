# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0011_auto_20160306_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenthremploy',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studenthremploy',
            name='last_change',
            field=models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4e00\u6b21\u4fee\u6539\u65f6\u95f4'),
            preserve_default=True,
        ),
    ]
