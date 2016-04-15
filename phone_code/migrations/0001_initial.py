# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneCode',
            fields=[
                ('phone', models.CharField(max_length=11, serialize=False, verbose_name='\u624b\u673a\u53f7\u7801', primary_key=True)),
                ('code', models.CharField(max_length=10, verbose_name='\u9a8c\u8bc1\u7801')),
                ('time_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u751f\u6210\u65f6\u523b')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
