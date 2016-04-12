# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0017_auto_20160411_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='group',
            field=models.CharField(default='\u672a\u5206\u7ec4', max_length=128, verbose_name='\u6807\u7b7e\u5206\u7ec4', choices=[('TIE\u6d4b\u8bc4', 'TIE\u6d4b\u8bc4'), ('\u672a\u5206\u7ec4', '\u672a\u5206\u7ec4')]),
            preserve_default=True,
        ),
    ]
