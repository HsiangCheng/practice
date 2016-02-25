# --coding: utf-8--
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from api.v1.permissions import IsHrOrReadOnly, IsOwner, IsOwnerOrReadOnly
from api.v1.recruit.serializers import RecruitSerializer
from webuser.models import Hr, RecruitInfo


class RecruitListAPIView(CreateModelMixin, ListModelMixin, GenericAPIView):
    serializer_class = RecruitSerializer
    queryset = RecruitInfo.objects.all()
    permission_classes = (IsHrOrReadOnly, )

    def get(self, request):
        """
        获取招聘信息列表
        """
        return self.list(request)

    def post(self, request):
        """
        发布招聘信息（需Hr登录）
        ---
        omit_parameters:
            - form
        parameters:
            - name: Authorization
              paramType: header
              required: True
              type: string
            - name: body
              type: WriteRecruitSerializer
              paramType: body
        """
        return self.create(request)

    def create(self, request, *args, **kwargs):
        data = dict(request.data)
        owner = Hr.objects.get(user=request.user)
        data['owner'] = owner.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class RecruitDetailAPIView(UpdateModelMixin, RetrieveModelMixin, GenericAPIView):
    serializer_class = RecruitSerializer
    queryset = RecruitInfo.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )

    def get(self, request, pk=None):
        """
        获取一条招聘信息
        ---
        """
        return self.retrieve(request)

    def patch(self, request, pk=None):
        """
        修改一条招聘信息（需拥有者登录）
        ---
        parameters:
            - name: Authorization
              paramType: header
              required: True
              type: string
              description: 用户的验证令牌，填写格式：Token *********
        """
        return self.partial_update(request)


