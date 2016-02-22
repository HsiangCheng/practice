# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0002_auto_20160208_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=60, verbose_name='\u516c\u53f8\u540d\u79f0', blank=True)),
                ('company_profile', models.TextField(verbose_name='\u516c\u53f8\u7b80\u4ecb', blank=True)),
                ('phone', models.CharField(max_length=12, verbose_name='\u8054\u7cfb\u65b9\u5f0f', blank=True)),
                ('owner', models.OneToOneField(related_name='company', to='webuser.Hr')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='hr',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='company_profile',
        ),
        migrations.AlterField(
            model_name='resume',
            name='owner',
            field=models.OneToOneField(related_name='resume', null=True, to='webuser.Student'),
            preserve_default=True,
        ),
    ]
