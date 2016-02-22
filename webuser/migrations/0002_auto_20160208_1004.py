# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='label',
        ),
        migrations.RemoveField(
            model_name='student',
            name='resume',
        ),
        migrations.AddField(
            model_name='label',
            name='student',
            field=models.ManyToManyField(related_name='labels', to='webuser.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resume',
            name='owner',
            field=models.OneToOneField(related_name='resumes', null=True, to='webuser.Student'),
            preserve_default=True,
        ),
    ]
