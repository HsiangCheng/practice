# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0003_auto_20160208_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='time_of_enrollment',
            field=models.SmallIntegerField(default=0, error_messages={b'max_value': '\u5fc5\u987b\u5c0f\u4e8e\u7b49\u4e8e2016\u5e74', b'min_value': '\u5fc5\u987b\u5927\u4e8e\u7b49\u4e8e1890\u5e74'}, verbose_name='\u5165\u5b66\u65f6\u95f4', blank=True, validators=[django.core.validators.MaxValueValidator(2016), django.core.validators.MinValueValidator(1890)]),
            preserve_default=True,
        ),
    ]
