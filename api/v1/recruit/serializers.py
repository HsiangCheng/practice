# --coding: utf-8--
from rest_framework import serializers
from webuser.models import RecruitInfo, Hr

class CurrentHrDefault(serializers.CurrentUserDefault):
    def set_context(self, serializer_field):
        self.user = serializer_field.context['request'].user.hr


class RecruitSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='owner.company_name')
    company_profile = serializers.ReadOnlyField(source='owner.company_profile')
    phone = serializers.ReadOnlyField(source='owner.phone')
    owner = serializers.HiddenField(default=CurrentHrDefault())

    class Meta:
        model = RecruitInfo
