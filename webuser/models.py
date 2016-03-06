# --coding: utf-8--
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.core import validators
from django.db import models, IntegrityError
from django.utils import timezone

# Create your models here.
from django.db.models import Manager
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import time


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Resume(models.Model):
    max_year = time.localtime().tm_year
    min_year = 1890
    owner = models.OneToOneField('Student', related_name='resume', null=True)
    school = models.CharField(verbose_name=u'学校', max_length=30, blank=True)
    time_of_enrollment = models.SmallIntegerField(verbose_name=u'入学时间',
                                                  validators=[
                                                      validators.MaxValueValidator(max_year),
                                                      validators.MinValueValidator(min_year),
                                                  ],
                                                  error_messages={
                                                      'max_value': u'必须小于等于%d年' % max_year,
                                                      'min_value': u'必须大于等于%d年' % min_year,
                                                  },
                                                  blank=True,
                                                  default=0)
    political_status = models.CharField(verbose_name=u'政治面貌', max_length=10, blank=True)
    position = models.TextField(verbose_name=u'担任职务', blank=True)
    award_certificate = models.TextField(verbose_name=u'获奖证书', blank=True)
    professional_certificate = models.TextField(verbose_name=u'专业证书', blank=True)
    speciality = models.TextField(verbose_name=u'技能特长', blank=True)
    job_intension = models.CharField(verbose_name=u'求职意向', max_length=60, blank=True)


class Label(models.Model):
    student = models.ManyToManyField('Student', related_name='labels')
    name = models.CharField(verbose_name=u'标签名称', max_length=128, unique=True)

    def __unicode__(self):
        return u'%s' % self.name


class StudentManager(Manager):
    def create_student(self, username, email=None,
                       password=None, name=None,
                       sex=None, phone=None, **extra_fields):
        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            raise validators.ValidationError('User with this username already exists.',
                                             code='unique')
        group, created = Group.objects.get_or_create(name='student')
        user.groups.add(group)
        student = self.create(user=user, name=name or '',
                              sex=sex or '', phone=phone or '',
                              **extra_fields)
        Resume.objects.create(owner=student)
        return student


class Student(models.Model):
    MALE = u'男'
    FEMALE = u'女'
    SECRET = u'保密'
    NONE = u''
    SEX_CHOICES = (
        (MALE, u'男'),
        (FEMALE, u'女'),
        (SECRET, u'保密'),
    )
    user = models.OneToOneField(User, related_name='student')
    name = models.CharField(verbose_name=u"姓名", max_length=30, blank=True)
    sex = models.CharField(verbose_name=u'性别', max_length=4,
                           choices=SEX_CHOICES, default=NONE)
    phone = models.CharField(verbose_name=u'手机号码', max_length=11, blank=True)

    objects = StudentManager()

    def delete(self, using=None):
        user = self.user
        super(Student, self).delete()
        user.delete()

    def __unicode__(self):
        return u'%s' % self.user.username


class HrManager(Manager):
    def create_hr(self, username, email=None, password=None, **extra_fields):
        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            raise validators.ValidationError('User with this username already exists.',
                                             code='unique')
        group, created = Group.objects.get_or_create(name='hr')
        user.groups.add(group)
        hr = self.create(user=user, **extra_fields)
        CompanyInfo.objects.create(owner=hr)
        return hr


class Hr(models.Model):
    user = models.OneToOneField(User, related_name='hr')
    target = models.ManyToManyField('Student',
                                    through='StudentHrEmploy',
                                    through_fields=('hr', 'student'))
    objects = HrManager()

    def delete(self, using=None):
        user = self.user
        super(Hr, self).delete()
        user.delete()


class CompanyInfo(models.Model):
    owner = models.OneToOneField('Hr', verbose_name=u'拥有者', related_name='company')
    company_name = models.CharField(verbose_name=u'公司名称', max_length=60, blank=True)
    company_profile = models.TextField(verbose_name=u'公司简介', blank=True)
    phone = models.CharField(verbose_name=u'联系方式', max_length=15, blank=True)


class RecruitInfo(models.Model):
    owner = models.ForeignKey('Hr', verbose_name=u'拥有者', related_name='recruit')
    position = models.CharField(verbose_name=u'招聘岗位', max_length=60, blank=True)
    recruiting_number = models.IntegerField(verbose_name=u'招聘人数', blank=True)
    educational_requirement = models.CharField(verbose_name=u'学历要求', max_length=60, blank=True)
    position_description = models.TextField(verbose_name=u'职位说明', blank=True)
    job_location = models.CharField(verbose_name=u'工作地点', max_length=120, blank=True)


class StudentHrEmploy(models.Model):
    STUDENT = u'学生'
    HR = u'HR'
    MASTER_CHOICES = (
        (STUDENT, u'学生'),
        (HR, u'HR')
    )
    AGREEMENT = u'同意'
    DISAGREEMENT = u'拒绝'
    NO_REPLY = u'未答复'
    STATUS_CHOICES = (
        (AGREEMENT, u'同意'),
        (DISAGREEMENT, u'拒绝'),
        (NO_REPLY, u'未答复')
    )
    student = models.ForeignKey('Student', verbose_name=u'学生', related_name='employs', blank=False)
    hr = models.ForeignKey('Hr', verbose_name=u'HR', related_name='employs', blank=False)
    recruit = models.ForeignKey('RecruitInfo', verbose_name=u'招聘信息', related_name='employs', blank=False)
    master = models.CharField(verbose_name=u'主动方', max_length=10, choices=MASTER_CHOICES, blank=True)
    status = models.CharField(verbose_name=u'状态', max_length=10, choices=STATUS_CHOICES, default=NO_REPLY)
    date_joined = models.DateTimeField(verbose_name=u'添加时间', auto_now_add=timezone.now())
    last_change = models.DateTimeField(verbose_name=u'最后一次修改时间', auto_now=timezone.now())

    class Meta:
        # db_table以后需要考虑写成动态的
        db_table = 'webuser_student_hr_employ'
        unique_together = ('student', 'hr', 'recruit')

