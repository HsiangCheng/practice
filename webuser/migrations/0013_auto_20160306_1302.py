# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0012_auto_20160306_1230'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='studenthremploy',
            table='webuser_student_hr_employ',
        ),
    ]
