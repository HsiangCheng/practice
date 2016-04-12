# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0016_auto_20160411_0130'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tiereply',
            unique_together=set([('student', 'question')]),
        ),
    ]
