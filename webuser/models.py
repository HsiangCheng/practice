# --coding: utf-8--
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Student(models.Model):
    user = models.OneToOneField(User)
    full_name = models.CharField(u"真实姓名", max_length=30, blank=True)

    class Meta:
        permissions = (
            ("view_student", u"可以查看学生信息"),
        )

class Hr(models.Model):
    user = models.OneToOneField(User)
    full_name = models.CharField(u'真实姓名', max_length=30, blank=True)

    class Meta:
        permissions = (
            ("view_hr", u"可以查看HR信息"),
        )

# class Resume(models.Model):
#     owner = models.OneToOneField(Student)
#     reviewer = models.ManyToManyField(Hr)
#
#     class Meta:
#         permissions = (
#             ("view_resume", u"可以查看简历信息"),
#         )
