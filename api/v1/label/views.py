# --coding: utf-8
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from api.v1.label.serializers import LabelSerializer
from webuser.models import Label


class LabelListAPIView(ListModelMixin, GenericAPIView):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()

    def get(self, request):
        """
        获取标签列表
        ---
        """
        return self.list(request)

