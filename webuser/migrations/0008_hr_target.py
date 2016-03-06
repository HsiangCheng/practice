# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0007_auto_20160304_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='hr',
            name='target',
            field=models.ManyToManyField(to='webuser.Student', through='webuser.StudentHrEmploy'),
            preserve_default=True,
        ),
    ]
