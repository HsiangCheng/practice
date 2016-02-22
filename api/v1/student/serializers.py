# --coding: utf-8--
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from rest_framework import serializers
from webuser.models import Student, Resume

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        exclude = ('owner', )
        read_only_fields = ('id',)


class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username',
                                     max_length=30,
                                     read_only=True,
                                     validators=[
                                         RegexValidator(r'^[\w.@+-]+$', 'Enter a valid username.', 'invalid')
                                     ])
    email = serializers.EmailField(source='user.email', required=False)
    resume = ResumeSerializer(many=False)

    class Meta:
        model = Student
        exclude = ('user', )
        read_only_fields = ('id',)

    def validate_username(self, value):
        if User.objects.filter(username=value).count() > 0:
            raise serializers.ValidationError("User with this username already exists.")
        return value

    def create(self, validated_data):
        data = dict(validated_data)
        data.update(data.pop('user'))
        instance = self.Meta.model.objects.create_student(**data)
        return instance

    def update(self, instance, validated_data):
        data = validated_data.copy()
        # user
        if data.has_key('user') and data['user'].has_key('email'):
            instance.user.email = data.pop('user').get('email')
            instance.user.save()
        # resume
        if data.has_key('resume'):
            resume_data = data.pop('resume')
            for attr, value in resume_data.items():
                setattr(instance, attr, value)
            instance.save()
        super(StudentSerializer, self).update(instance, data)
        return instance