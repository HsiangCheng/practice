# --coding: utf-8--
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from rest_framework import serializers
from api.v1.recruit.serializers import CurrentHrDefault
from webuser.models import Hr, CompanyInfo, StudentHrEmploy


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        exclude = ('owner', )


class HrSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username',
                                     max_length=30,
                                     read_only=True,
                                     validators=[
                                         RegexValidator(r'^[\w.@+-]+$', 'Enter a valid username.', 'invalid')
                                     ])
    email = serializers.EmailField(source='user.email', required=False)
    company = CompanySerializer(many=False)

    class Meta:
        model = Hr
        exclude = ('user', 'targets', )
        read_only_fields = ('id',)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("User with this username already exists.")
        return value

    def create(self, validated_data):
        data = dict(validated_data)
        data.update(data.pop('user'))
        instance = self.Meta.model.objects.create_hr(**data)
        return instance

    def update(self, instance, validated_data):
        data = validated_data.copy()
        # user
        if data.has_key('user') and data['user'].has_key('email'):
            instance.user.email = data.pop('user').get('email')
            instance.user.save()
        # company
        if data.has_key('company'):
            company_data = data.pop('company')
            for attr, value in company_data.items():
                setattr(instance.company, attr, value)
            instance.company.save()
        super(HrSerializer, self).update(instance, data)
        return instance


class HrTargetSerializer(serializers.ModelSerializer):
    hr = serializers.HiddenField(default=CurrentHrDefault(), write_only=True)
    master = serializers.HiddenField(default=StudentHrEmploy.HR)
    status = serializers.CharField(default=StudentHrEmploy.NO_REPLY, read_only=True)
    date_joined = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    last_change = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    recruit_name = serializers.CharField(source='recruit.position', read_only=True)
    student_name = serializers.CharField(source='student.name', read_only=True)

    class Meta:
        model = StudentHrEmploy
        # fields = '__all__'

    def validate_recruit(self, value):
        hr = self.context['request'].user.hr
        if not hr.recruits.filter(id=value.id).exists():
            raise serializers.ValidationError(u'该用户并未发表这条招聘信息')
        return value