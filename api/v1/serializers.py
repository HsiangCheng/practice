# --coding: utf-8--
from collections import OrderedDict

from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.fields import SkipField

from api.v1.exceptions import UniqueError
from webuser.models import *


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username_plus = serializers.CharField(source='username')
    class Meta:
        model = User
        fields = ( 'username','password' ,'email', 'username_plus',)


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128,write_only=True)

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=30,
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$', 'Enter a valid username.', 'invalid')
        ])
    password = serializers.CharField(max_length=128, write_only=True)
    email = serializers.EmailField(required=False)
    full_name =  serializers.CharField(max_length=30, required=False)

    student_field_names = ["full_name"]

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        user = instance.user
        readable_fields = self._readable_fields
        user_fields = [field for field in readable_fields
                       if field.field_name not in self.student_field_names]
        student_fields = [field for field in readable_fields
                       if field.field_name in self.student_field_names]

        for field in user_fields:
            try:
                attribute = field.get_attribute(instance.user)
            except SkipField:
                continue

            if attribute is None:
                # We skip `to_representation` for `None` values so that
                # fields do not have to explicitly deal with that case.
                ret[field.field_name] = None
            else:
                ret[field.field_name] = field.to_representation(attribute)


        for field in student_fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is None:
                # We skip `to_representation` for `None` values so that
                # fields do not have to explicitly deal with that case.
                ret[field.field_name] = None
            else:
                ret[field.field_name] = field.to_representation(attribute)

        return ret

    def create(self, validated_data):
        data = dict(validated_data)
        try:
            user = User.objects.create_user(username=data.get('username'), password=data.get('password'),
                                            email=data.get('email'))
        except IntegrityError as err:
            raise UniqueError(detail="user is existing")
        student_info = {"user": user}
        for key in self.student_field_names:
            value = data.get(key)
            if value is not None:
                student_info[key] = value
        return Student.objects.create(**student_info)

    def update(self, instance, validated_data):
        data = dict(validated_data)
        password = data.get("password")
        email = data.get("email")
        if password is not None:
            instance.user.set_password(password)
        if email is not None:
            instance.user.email = email
        for key in self.student_field_names:
            value = data.get(key)
            if value is not None:
                setattr(instance, key, value)
        instance.save()

        return instance



    # def validate_username(self, value):
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError("Blog post is not about Django")
    #     return value

class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        exclude = ('id', 'owner')

class HrSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username',
                                 max_length=30,
                                 validators=[
                                     validators.RegexValidator(r'^[\w.@+-]+$', 'Enter a valid username.', 'invalid')
                                 ])
    email = serializers.EmailField(source='user.email', required=False)
    password = serializers.CharField(source='user.password', max_length=128, write_only=True)
    groups = serializers.StringRelatedField(source='user.groups', many=True, read_only=True)
    company = CompanyInfoSerializer(many=False)

    class Meta:
        model = Hr
        fields = ('__all__')

    def validate_username(self, value):
        if User.objects.filter(username=value).count() > 0:
            raise serializers.ValidationError("User with this username already exists.")
        return value

    def create(self, validated_data):
        data = dict(validated_data)
        data.update(data.pop('user'))
        hr = Hr.objects.create_hr(**data)
        return hr

    # def update(self, instance, validated_data):



# from rest_framework import serializers
# from django.contrib.auth.models import User, Group
# from webuser.models import *
# # Serializers define the API representation.
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         # fields = ('url', 'username','password' ,'email', 'is_staff', 'groups')
#         fields = ('url', 'username','password' ,'email',)
#         # fields = '__all__'
#
#     # def create(self, validated_data):
#     #     super(UserSerializer, self).create(**validated_data)
#
#     # extra_kwargs = {
#     #     'url': {'view_name': 'accounts', 'lookup_field': 'account_name'},
#     #     'username': {'lookup_field': 'username'}
#     # }
#
#
# class StudentSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=False)
#     # user = serializers.PrimaryKeyRelatedField()
#     class Meta:
#         model = UserInfo
#         fields = ('__all__')
#         # extra_kwargs = {'username': {}, 'email': {},  'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user_data = validated_data.pop('user')
#         user = User.objects.create(**user_data)
#         user.set_password(user_data['password'])
#         user.save()
#         student = UserInfo.objects.create(user=user, **validated_data)
#         return student
#         # def create(self, validated_data):
#         #     user = User(
#         #         email=validated_data['email'],
#         #         username=validated_data['username']
#         #     )
#         #     user.set_password(validated_data['password'])
#         #     user.save()
#         #
#         #     student = UserInfo(
#         #         full_name=validated_data['full_name'],
#         #         user = user.id
#         #     )
#         #     student.save()
#         #
#         #     return student
#
#
#
# # Again
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'id', 'name')
#
# class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = UserInfo
#         fields = ('url', 'user', "full_name")
#         depth = 0
#
# class ResumeSerializer(serializers.HyperlinkedModelSerializer):
#     # owner = serializers.Field(source='owner.username')
#
#     class Meta:
#         model = Resume
#         fields = ('url', 'owner', 'name')