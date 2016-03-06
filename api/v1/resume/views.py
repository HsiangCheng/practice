# --coding: utf-8--
from django.contrib.auth.models import Group
from django.db.models import Q
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from api.v1.permissions import IsHr, IsHrOrOwner
from api.v1.resume.serializers import ResumeFullSerializer
from webuser.models import Resume

class ResumeListAPIView(ListModelMixin, GenericAPIView):
    serializer_class = ResumeFullSerializer
    queryset = Resume.objects.all()
    permission_classes = (IsHr, )

    def get_queryset(self):
        queryset = Resume.objects.all()
        label_ids = self.request.query_params.get('labelIds', None)
        if isinstance(label_ids, unicode):
            label_ids = label_ids.split(u',')
            for label_id in label_ids:
                queryset = queryset.filter(owner__labels=label_id)
        return queryset



    def get(self, request):
        """
        获取简历列表（需Hr登录）
        ---
        parameters:
            - name: Authorization
              paramType: header
              required: True
              type: string
              description: 用户的验证令牌，填写格式：Token *********
            - name: labelIds
              paramType: query
              required: False
              type: string
              description: 根据标签id筛选简历，多个标签用逗号分割
        """
        return self.list(request)

class ResumeDetailAPIView(RetrieveModelMixin, GenericAPIView):
    serializer_class = ResumeFullSerializer
    queryset = Resume.objects.all()
    permission_classes = (IsHrOrOwner, )

    def get(self, request, pk=None):
        """
        获取一个简历（需Hr登录或者拥有者登录）
        ---
        parameters:
            - name: Authorization
              paramType: header
              required: True
              type: string
              description: 用户的验证令牌，填写格式：Token *********
        """
        return self.retrieve(request)

