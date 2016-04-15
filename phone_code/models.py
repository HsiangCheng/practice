# -*-coding: utf-8-*-
import random

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone
from django.conf import settings


class PhoneCodeManager(models.Manager):

    def get_or_update_phone_code(self, phone):
        # 获取PhoneCode对象, 不存在则创建
        try:
            phone_code = self.get(phone=phone)
        except ObjectDoesNotExist as err:
            code = self._get_code()
            phone_code = self.create(phone=phone, code=code, time_joined=timezone.now())
        # 检查记录是否已超时, 超时则更新code
        if phone_code.is_timeout():
            phone_code.code = self._get_code()
            phone_code.time_joined = timezone.now()
            phone_code.save()
        return phone_code

    @staticmethod
    def _get_code():
        code_sample = [unicode(num) for num in range(0, 10, 1)]
        code = ''.join(random.sample(code_sample, 6))
        return code

    def check_code(self, phone, code):
        # 手机号是否存在
        try:
            phone_code = self.get(phone=phone)
        except ObjectDoesNotExist as err:
            return False
        # 是否超时
        if phone_code.is_timeout():
            return False
        # 是否相同
        return code == phone_code.code


class PhoneCode(models.Model):
    phone = models.CharField(verbose_name=u'手机号码', max_length=11, primary_key=True)
    code = models.CharField(verbose_name=u'验证码', max_length=10)
    time_joined = models.DateTimeField(verbose_name=u'生成时刻', default=timezone.now)

    objects = PhoneCodeManager()

    def __init__(self, *args, **kwargs):
        self._timeout = self.load_timeout()
        super(PhoneCode, self).__init__(*args, **kwargs)

    def is_timeout(self):
        time_now = timezone.now()
        time_joined = self.time_joined
        return (time_now - time_joined).seconds > self._timeout

    @property
    def timeout(self):
        return self._timeout

    @staticmethod
    def load_timeout():
        timeout = 60
        try:
            timeout = settings.PHONE_CODE_TIMEOUT
        except NameError as err:
            pass
        return timeout



