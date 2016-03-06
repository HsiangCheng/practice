# --coding: utf-8
from rest_framework import serializers

from webuser.models import Label


class LabelSerializer(serializers.ModelSerializer):
    # student = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Label
        exclude = ('student', )



