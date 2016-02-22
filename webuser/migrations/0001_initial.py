# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=60, verbose_name='\u516c\u53f8\u540d\u79f0', blank=True)),
                ('company_profile', models.TextField(verbose_name='\u516c\u53f8\u7b80\u4ecb', blank=True)),
                ('user', models.OneToOneField(related_name='hr', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u6807\u7b7e\u540d\u79f0')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecruitInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=60, verbose_name='\u62db\u8058\u5c97\u4f4d', blank=True)),
                ('recruiting_number', models.IntegerField(verbose_name='\u62db\u8058\u4eba\u6570', blank=True)),
                ('educational_requirement', models.CharField(max_length=60, verbose_name='\u5b66\u5386\u8981\u6c42', blank=True)),
                ('position_description', models.TextField(verbose_name='\u804c\u4f4d\u8bf4\u660e', blank=True)),
                ('job_location', models.CharField(max_length=120, verbose_name='\u5de5\u4f5c\u5730\u70b9', blank=True)),
                ('owner', models.ForeignKey(related_name='hr', to='webuser.Hr')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(max_length=30, verbose_name='\u5b66\u6821', blank=True)),
                ('time_of_enrollment', models.SmallIntegerField(blank=True, error_messages={b'max_value': '\u5fc5\u987b\u5c0f\u4e8e\u7b49\u4e8e2016\u5e74', b'min_value': '\u5fc5\u987b\u5927\u4e8e\u7b49\u4e8e1890\u5e74'}, verbose_name='\u5165\u5b66\u65f6\u95f4', validators=[django.core.validators.MaxValueValidator(2016), django.core.validators.MinValueValidator(1890)])),
                ('political_status', models.CharField(max_length=10, verbose_name='\u653f\u6cbb\u9762\u8c8c', blank=True)),
                ('position', models.TextField(verbose_name='\u62c5\u4efb\u804c\u52a1', blank=True)),
                ('award_certificate', models.TextField(verbose_name='\u83b7\u5956\u8bc1\u4e66', blank=True)),
                ('professional_certificate', models.TextField(verbose_name='\u4e13\u4e1a\u8bc1\u4e66', blank=True)),
                ('speciality', models.TextField(verbose_name='\u6280\u80fd\u7279\u957f', blank=True)),
                ('job_intension', models.CharField(max_length=60, verbose_name='\u6c42\u804c\u610f\u5411', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u59d3\u540d', blank=True)),
                ('sex', models.CharField(default='\u4fdd\u5bc6', max_length=4, verbose_name='\u6027\u522b', choices=[('\u7537', '\u7537'), ('\u5973', '\u5973'), ('\u4fdd\u5bc6', '\u4fdd\u5bc6')])),
                ('phone', models.CharField(max_length=11, verbose_name='\u624b\u673a\u53f7\u7801', blank=True)),
                ('label', models.ManyToManyField(related_name='students', to='webuser.Label')),
                ('resume', models.OneToOneField(related_name='student', null=True, to='webuser.Resume')),
                ('user', models.OneToOneField(related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
