# --coding: utf-8--
from rest_framework import serializers
from django.contrib.auth.models import User
from webuser.models import *

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ( 'username','password' ,'email',)

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ('user', 'full_name')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data['password'])
        user.save()
        student = Student.objects.create(user=user, **validated_data)
        return student

class HrSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Hr
        fields = ('user', 'full_name')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data['password'])
        user.save()
        hr = Hr.objects.create(user=user, **validated_data)
        return hr


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