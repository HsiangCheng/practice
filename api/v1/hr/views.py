# --coding: utf-8--
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, ListModelMixin, CreateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from api.v1.hr.serializers import HrSerializer, HrTargetSerializer
from api.v1.permissions import IsUser, IsHr
from webuser.models import Hr, StudentHrEmploy


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


class HrTargetListAPIView(CreateModelMixin, ListModelMixin, GenericAPIView):
    serializer_class = HrTargetSerializer
    queryset = StudentHrEmploy.objects.all()
    # lookup_field = 'user__username'
    # lookup_url_kwarg = 'username'
    permission_classes = (IsHr, )

    def get_queryset(self):
        hr = self.request.user.hr
        return StudentHrEmploy.objects.filter(hr=hr)

    # get
    def get(self, request, username=None):
        """
        获取HR的目标列表（需用户自己登录）
        ---
        parameters:
            - name: Authorization
              paramType: header
              type: string
              required: True
              description: 用户的验证令牌，填写格式：Token *********
        """
        return self.list(request)

    # post
    def post(self, request, username=None):
        """
        添加一个目标（需用户自己登录）
        ---
        parameters:
            - name: Authorization
              paramType: header
              type: string
              required: True
              description: 用户的验证令牌，填写格式：Token *********
            - name: student
              paramType: form
              type: integer
              required: True
            - name: recruit
              paramType: form
              type: integer
              required: True
        """
        return self.create(request)


class HrTargetDetailAPIView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    serializer_class = HrTargetSerializer
    queryset = StudentHrEmploy.objects.all()
    permission_classes = (IsHr, )

    def get_queryset(self):
        hr = self.request.user.hr
        return StudentHrEmploy.objects.filter(hr=hr)

    # get
    def get(self, request, pk=None):
        """
        获取一个HR目标（需用户自己登录）
        ---
        parameters:
            - name: Authorization
              paramType: header
              type: string
              required: True
              description: 用户的验证令牌，填写格式：Token *********
        """
        return self.retrieve(request)

    # patch
    def patch(self, request, pk=None):
        """
        修改一个目标信息（需用户自己登录）
        ---
        parameters:
            - name: Authorization
              paramType: header
              type: string
              required: True
              description: 用户的验证令牌，填写格式：Token *********
        """
        return self.partial_update(request)

    # delete
    def delete(self, request, pk=None):
        """
        删除一个目标（需用户自己登录）
        ---
        parameters:
            - name: Authorization
              paramType: header
              type: string
              required: True
              description: 用户的验证令牌，填写格式：Token *********
        """
        return self.destroy(request)


