# --coding: utf-8--
from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core import validators
from webuser.models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label=u'账号',
                               error_messages={'required': u'请输入账号',
                                               'max_length': u'账号长度应小于%(limit_value)d',
                                               'invalid': u'账号中不能含有“@ . + - _”以外的特殊字符'
                                               },
                               validators=[
                                   validators.RegexValidator(r'^[\w.@+-]+$', 'Enter a valid username.', 'invalid')
                               ])
    password = forms.CharField(max_length=128, widget=forms.PasswordInput,
                               label=u'密码', error_messages={'required': u'请输入密码'})

    error_messages = {
        'inexistent_user': u'该用户不存在',
        'wrong_password': u'密码错误',
        'inactive': u'用户尚未激活',
    }

    def __init__(self, request=None, *args, **kwargs):
        kwargs['auto_id'] = '%s'
        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

        self.UserModel = Hr


    def clean_username(self):
        # if self. == 'admin' and self.password == 'admin':
        #     return True
        # else:
        username = self.cleaned_data.get('username')
        if not self.UserModel.objects.filter(user__username=username).exists():
            raise forms.ValidationError(
                self.error_messages['inexistent_user'],
                code='inexistent_user'
            )
        return username

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                self.add_error(
                    'password',
                    self.error_messages['wrong_password']
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


