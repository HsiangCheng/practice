# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0005_auto_20160304_0956'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='studenthremploy',
            table='student_hr_employ',
        ),
    ]
