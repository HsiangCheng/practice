# --coding: utf-8--
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.fields import empty

from webuser.models import Student, Resume, Label, StudentHrEmploy, TIEReply, TIEQuestion


class CurrentStudentDefault(serializers.CurrentUserDefault):
    def set_context(self, serializer_field):
        self.user = serializer_field.context['request'].user.student


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        exclude = ('owner',)
        read_only_fields = ('id',)


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        exclude = ('student',)


class LabelAddSerializer(serializers.Serializer):
    model = Student
    # Write
    student = serializers.HiddenField(default=CurrentStudentDefault(), write_only=True)
    label_ids = serializers.CharField(write_only=True,
                                      validators=[
                                          RegexValidator(r'^[\w,]+$', u'格式不合法', 'invalid')
                                      ])
    # Read
    labels = LabelSerializer(many=True, read_only=True)

    # def validate_student(self, value):
    #     if not self.model.objects.filter(user__username=value).exists():
    #         raise serializers.ValidationError(u'用户不存在')
    #     return value

    def create(self, validated_data):
        instance = validated_data['student']
        label_ids = validated_data['label_ids']
        label_ids = label_ids.split(',')
        for label_id in label_ids:
            instance.labels.add(int(label_id))
        return instance


class StudentInvitationSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    last_change = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    recruit_name = serializers.CharField(source='recruit.position', read_only=True)
    company_name = serializers.CharField(source='hr.company.company_name', read_only=True)

    class Meta:
        model = StudentHrEmploy
        exclude = ('student', 'master')
        read_only_fields = ('hr', 'recruit')


class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username',
                                     max_length=30,
                                     read_only=True,
                                     validators=[
                                         RegexValidator(r'^[\w.@+-]+$', 'Enter a valid username.', 'invalid')
                                     ])
    email = serializers.EmailField(source='user.email', required=False)
    resume = ResumeSerializer(many=False)

    # labels = LabelSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        exclude = ('user',)
        read_only_fields = ('id',)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
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
                setattr(instance.resume, attr, value)
            instance.resume.save()
        super(StudentSerializer, self).update(instance, data)
        return instance

#
# class TIEReplyListSerializer(serializers.ListSerializer):
#     pass


class TIEReplySerializer(serializers.ModelSerializer):
    # student = serializers.HiddenField(default=CurrentStudentDefault, write_only=True)
    # student = serializers.CharField()
    # question = serializers.CharField()
    # reply = serializers.CharField()

    # def __init__(self, instance=None, data=empty, **kwargs):
    #     kwargs['many'] = True
    #     super(TIEReplySerializer, self).__init__(instance, data, **kwargs)

    class Meta:
        model = TIEReply
        # list_serializer_class = TIEReplyListSerializer





class TIEQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TIEQuestion
        exclude = ('student',)
