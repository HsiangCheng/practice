# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0009_auto_20160305_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='\u8054\u7cfb\u65b9\u5f0f', blank=True),
            preserve_default=True,
        ),
    ]
