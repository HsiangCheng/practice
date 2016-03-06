# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0004_auto_20160216_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentHrEmploy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hr', models.ForeignKey(related_name='employs', verbose_name='HR', to='webuser.Hr')),
                ('recruit', models.ForeignKey(related_name='employs', verbose_name='\u62db\u8058\u4fe1\u606f', to='webuser.RecruitInfo')),
                ('student', models.ForeignKey(related_name='employs', verbose_name='\u5b66\u751f', to='webuser.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='studenthremploy',
            unique_together=set([('student', 'hr', 'recruit')]),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='owner',
            field=models.OneToOneField(related_name='company', verbose_name='\u62e5\u6709\u8005', to='webuser.Hr'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recruitinfo',
            name='owner',
            field=models.ForeignKey(related_name='recruit', verbose_name='\u62e5\u6709\u8005', to='webuser.Hr'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(default='', max_length=4, verbose_name='\u6027\u522b', choices=[('\u7537', '\u7537'), ('\u5973', '\u5973'), ('\u4fdd\u5bc6', '\u4fdd\u5bc6')]),
            preserve_default=True,
        ),
    ]
