# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0008_hr_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(unique=True, max_length=128, verbose_name='\u6807\u7b7e\u540d\u79f0'),
            preserve_default=True,
        ),
    ]
