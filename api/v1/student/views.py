# --coding: utf-8--
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from api.v1.permissions import IsUser, IsStudent, IsOwner
from api.v1.student.serializers import StudentSerializer, LabelAddSerializer, StudentInvitationSerializer
from webuser.models import Student, Label, StudentHrEmploy


class StudentDetailAPIView(UpdateModelMixin, RetrieveModelMixin, GenericAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'
    permission_classes = (IsUser, IsStudent, )

    def get(self, request, username):
        """
        获取学生用户自己的信息（需用户自己登录）
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
        修改学生用户自己的信息（需用户自己登录）
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
              type: WriteStudentSerializer

        """
        return self.partial_update(request)


class StudentLabelAPIView(CreateModelMixin, RetrieveModelMixin, GenericAPIView):
    serializer_class = LabelAddSerializer
    queryset = Student.objects.all()
    # lookup_field = 'user__username'
    # lookup_url_kwarg = 'username'
    permission_classes = (IsUser, IsStudent, )

    def get_object(self):
        return self.request.user.student

    def get(self, request):
        """
        获取学生用户自己所有的标签（需用户自己登录）
        ---
        parameters:
            - name: Authorization
              paramType: header
              required: True
              type: string
              description: 用户的验证令牌，填写格式：Token *********
        """
        return self.retrieve(request)

    def post(self, request):
        """
        为学生用户添加一个标签（需用户自己登录）
        ---
        parameters:
            - name: Authorization
              paramType: header
              required: True
              type: string
              description: 用户的验证令牌，填写格式：Token *********

        """

        return self.create(request)


class StudentLabelDeleteAPIView(RetrieveModelMixin, GenericAPIView):
    serializer_class = LabelAddSerializer
    queryset = Student.objects.all()
    # lookup_field = 'user__username'
    # lookup_url_kwarg = 'username'
    permission_classes = (IsUser, IsStudent, )

    def get_object(self):
        return self.request.user.student

    # def get(self, request, label_id):
    #     return self.retrieve(request)

    def delete(self, request, label_id):
        """
        删除学生自己的一个标签（需用户自己登录）
        ---
        parameters:
            - name: Authorization
              paramType: header
              required: True
              type: string
              description: 用户的验证令牌，填写格式：Token *********
        """
        instance = self.get_object()
        # try:
        #     label = instance.labels.get(id=label_id)
        # except ObjectDoesNotExist as err:
        #     return Response({'error': u'指定标签不存在'})
        instance.labels.remove(label_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentInvitationListAPIView(ListModelMixin, GenericAPIView):
    serializer_class = StudentInvitationSerializer
    queryset = StudentHrEmploy.objects.all()
    # lookup_field = 'user__username'
    # lookup_url_kwarg = 'username'
    permission_classes = (IsUser, IsStudent, )

    def get_queryset(self):
        student = self.request.user.student
        return StudentHrEmploy.objects.filter(student=student)

    # get
    def get(self, request):
        """
        获取学生收到的邀请列表（需用户自己登录）
        ---
        parameters:
            - name: Authorization
              paramType: header
              required: True
              type: string
              description: 用户的验证令牌，填写格式：Token *********
        """
        return self.list(request)


class StudentInvitationDetailAPIView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    serializer_class = StudentInvitationSerializer
    queryset = StudentHrEmploy.objects.all()
    permission_classes = (IsStudent, )

    def get_queryset(self):
        student = self.request.user.student
        return StudentHrEmploy.objects.filter(student=student)

    # get
    def get(self, request, pk=None):
        """
        获取学生的一条邀请（需用户自己登录）
        ---
        parameters:
            - name: Authorization
              paramType: header
              required: True
              type: string
              description: 用户的验证令牌，填写格式：Token *********
        """
        return self.retrieve(request)
    # patch

    def patch(self, request, pk=None):
        """
        修改学生的一条邀请状态（需用户自己登录）
        ---
        parameters:
            - name: Authorization
              paramType: header
              required: True
              type: string
              description: 用户的验证令牌，填写格式：Token *********
        """
        return self.partial_update(request)



