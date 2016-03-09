# --coding: utf-8--
from rest_framework import serializers
from webuser.models import Resume


class ResumeFullSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(source='owner.id')
    name = serializers.ReadOnlyField(source='owner.name')
    sex = serializers.ReadOnlyField(source='owner.sex')
    phone = serializers.ReadOnlyField(source='owner.phone')
    email = serializers.ReadOnlyField(source='owner.user.email')
    labels = serializers.StringRelatedField(source='owner.labels', many=True)
    class Meta:
        model = Resume
        exclude = ('owner', )
        read_only_fields = ('__all__',)


