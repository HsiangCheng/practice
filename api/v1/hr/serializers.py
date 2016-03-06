# --coding: utf-8--
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from rest_framework import serializers
from webuser.models import Hr, CompanyInfo


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
        exclude = ('user', 'target', )
        read_only_fields = ('id',)

    def validate_username(self, value):
        if User.objects.filter(username=value).count() > 0:
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
