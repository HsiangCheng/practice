# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0014_auto_20160307_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='TIEQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField(verbose_name='\u95ee\u9898')),
            ],
            options={
                'db_table': 'webuser_tie_question',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TIEReply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reply', models.CharField(default='', max_length=10, verbose_name='\u56de\u7b54', choices=[('\u662f', '\u662f'), ('\u5426', '\u5426'), ('', '\u7a7a')])),
                ('question', models.ForeignKey(verbose_name='TIE\u95ee\u9898', to='webuser.TIEQuestion')),
                ('student', models.ForeignKey(verbose_name='\u5b66\u751f', to='webuser.Student')),
            ],
            options={
                'db_table': 'webuser_tie_reply',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tiequestion',
            name='student',
            field=models.ManyToManyField(related_name='tie_questions', through='webuser.TIEReply', to='webuser.Student'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recruitinfo',
            name='owner',
            field=models.ForeignKey(related_name='recruits', verbose_name='\u62e5\u6709\u8005', to='webuser.Hr'),
            preserve_default=True,
        ),
    ]
