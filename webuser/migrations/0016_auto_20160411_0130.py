# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0015_auto_20160411_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiequestion',
            name='id',
            field=models.IntegerField(serialize=False, verbose_name='\u9898\u76ee\u5e8f\u53f7', primary_key=True),
            preserve_default=True,
        ),
    ]
