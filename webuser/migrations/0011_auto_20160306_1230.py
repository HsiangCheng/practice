# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0010_auto_20160306_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenthremploy',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 6, 12, 30, 36, 764120, tzinfo=utc), verbose_name='\u6dfb\u52a0\u65f6\u95f4', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studenthremploy',
            name='last_change',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 6, 12, 30, 36, 764154, tzinfo=utc), verbose_name='\u6700\u540e\u4e00\u6b21\u4fee\u6539\u65f6\u95f4', auto_now=True),
            preserve_default=True,
        ),
    ]
