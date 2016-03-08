# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0013_auto_20160306_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hr',
            name='target',
        ),
        migrations.AddField(
            model_name='hr',
            name='targets',
            field=models.ManyToManyField(related_name='hrs', through='webuser.StudentHrEmploy', to='webuser.Student'),
            preserve_default=True,
        ),
    ]
