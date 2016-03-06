# --coding: utf-8--
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from api.v1.hr.serializers import HrSerializer
from api.v1.permissions import IsUser, IsHr
from webuser.models import Hr


class HrDetailAPIView(UpdateModelMixin, RetrieveModelMixin, GenericAPIView):
    serializer_class = HrSerializer
    queryset = Hr.objects.all()
    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'
    permission_classes = (IsUser, IsHr, )

    def get(self, request, username):
        """
        获取Hr用户自己的详细信息（需用户自己登录）
        ---
        parameters:
            - name: Authorization
              paramType: header
              required: True
              type: string
              description: 用户的验证令牌，填写格式：Token *********
        """
        return self.retrieve(request)

    def patch(self, request, username):
        """
        修改Hr用户自己的详细信息（需用户自己登录）
        ---
        omit_parameters:
            - form
        parameters:
            - name: Authorization
              paramType: header
              type: string
              required: True
              description: 用户的验证令牌，填写格式：Token *********
            - name: body
              paramType: body
              type: WriteHrSerializer
        """
        return self.partial_update(request)

