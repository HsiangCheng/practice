# --coding: utf-8--
from rest_framework import serializers
from webuser.models import Resume


class ResumeFullSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='owner.name')
    sex = serializers.ReadOnlyField(source='owner.sex')
    phone = serializers.ReadOnlyField(source='owner.phone')
    email = serializers.ReadOnlyField(source='owner.user.email')
    class Meta:
        model = Resume
        exclude = ('owner', )
        read_only_fields = ('__all__',)


