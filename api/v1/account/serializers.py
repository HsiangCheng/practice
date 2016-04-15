# --coding: utf-8--
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from rest_framework.fields import CharField, EmailField
from rest_framework.relations import StringRelatedField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from phone_code.models import PhoneCode
from webuser.models import Student, Hr


class StudentSignupSerializer(ModelSerializer):
    username = CharField(source='user.username',
                                 max_length=30,
                                 validators=[
                                     RegexValidator(r'^[\w.@+-]+$', 'Enter a valid username.', 'invalid')
                                 ])
    email = EmailField(source='user.email', required=False)
    password = CharField(source='user.password', max_length=128, write_only=True)
    code = CharField(write_only=True)

    class Meta:
        model = Student
        exclude = ('user', )
        read_only_fields = ('id', )

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(u'用户已存在')
        return value

    def validate_phone(self, value):
        if Student.objects.filter(phone=value).exists():
            raise serializers.ValidationError(u'手机号已存在')
        return value

    def validate(self, data):
        phone = data['phone']
        code = data['code']
        # 验证验证码
        if not PhoneCode.objects.check_code(phone, code):
            raise serializers.ValidationError({'code': u'验证码错误'})
        return data

    def create(self, validated_data):
        data = dict(validated_data)
        # 去除code
        data.pop('code')
        data.update(data.pop('user'))
        instance = self.Meta.model.objects.create_student(**data)
        return instance


class HrSignupSerializer(ModelSerializer):
    username = CharField(source='user.username',
                                 max_length=30,
                                 validators=[
                                     RegexValidator(r'^[\w.@+-]+$', 'Enter a valid username.', 'invalid')
                                 ])
    email = EmailField(source='user.email', required=False)
    password = CharField(source='user.password', max_length=128, write_only=True)

    class Meta:
        model = Hr
        exclude = ('user', )
        read_only_fields = ('id', )

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(u'用户已存在')
        return value

    def create(self, validated_data):
        data = dict(validated_data)
        data.update(data.pop('user'))
        instance = self.Meta.model.objects.create_hr(**data)
        return instance


class PasswordChangeSerializer(Serializer):
    # 这个序列化器只是为了向测试页面提供字段，并无实际用处
    password = CharField(source='user.password', max_length=128, write_only=True)
    new_password = CharField(source='user.password', max_length=128, write_only=True)


