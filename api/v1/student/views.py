# --coding: utf-8--
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from api.v1.permissions import IsUser, IsStudent, IsOwner
from api.v1.student.serializers import StudentSerializer, LabelAddSerializer, StudentInvitationSerializer, \
    TIEQuestionSerializer, TIEReplySerializer
from webuser.models import Student, Label, StudentHrEmploy, TIEQuestion, TIEReply

# TIE问卷回答数据到标签的映射
tie_label_mapping = {
    u'追求完美': {1: u'是', 5: u'否'},
    u'奉献主义': {2: u'是', 8: u'否'},
    u'实干要强': {3: u'否', 10: u'是'},
    u'浪漫艺术': {4: u'否', 6: u'是'},
    u'科学理性': {7: u'是', 12: u'否'},
    u'忠诚谨慎': {9: u'是', 18: u'否'},
    u'乐观活跃': {11: u'是', 17: u'是'},
    u'平和豁达': {13: u'否', 15: u'是'},
    u'敢闯敢当': {14: u'是', 16: u'否'},
}


def get_tie_label(reply):
    """
    这个函数传入一个TIE问卷填写的数据,
    返回对应的Label列表
    :param reply: key为tie_question_id, value为reply 的dict
    """
    labels = []
    # 遍历标签
    for label_name, conditions in tie_label_mapping.items():
        res = True
        # 遍历条件
        for condition_id, condition in conditions.items():
            if condition != reply.get(condition_id, None):
                res = False
                break
        # 条件全部符合
        if res:
            labels.append(Label.objects.get(name=label_name))
    return labels


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


class QuestionnaireAPIView(ListModelMixin, GenericAPIView):
    model = TIEQuestion
    serializer_class = TIEQuestionSerializer
    queryset = model.objects.all()

    def get(self, request):
        return self.list(request)


class TIEReplyAPIView(CreateModelMixin, GenericAPIView):
    model = TIEReply
    serializer_class = TIEReplySerializer
    queryset = model.objects.all()
    permission_classes = (IsStudent, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request):
        """
        提交一个问卷（需学生登录）
        ---
        omit_parameters:
            - form
        parameters:
            - name: Authorization
              paramType: header
              required: True
              type: string
              description: 用户的验证令牌，填写格式：Token *********
            - name: body
              paramType: body
              type: WriteTIEReplySerializer
        """
        for data in request.data:
            data['student'] = request.user.student.id
        response = self.create(request)
        # 更新Label
        reply = self._reply_list_to_dict(response.data)
        labels = get_tie_label(reply)
        for label in labels:
            request.user.student.labels.add(label)
        return response

    def _reply_list_to_dict(self, reply_list):
        reply_dict = {}
        for reply in reply_list:
            key = int(reply['question'])
            reply_dict[key] = reply['reply']
        return reply_dict


class TIEReplyCleanAPIView(GenericAPIView):
    permission_classes = (IsStudent, )

    def post(self, request):
        """
        !!测试使用!!完全清除TIE问卷的回复（需学生登录）
        ---
        parameters:
            - name: Authorization
              paramType: header
              required: True
              type: string
              description: 用户的验证令牌，填写格式：Token *********
        """
        student = self.request.user.student
        TIEReply.objects.filter(student=student).all().delete()
        student.labels.filter(group=Label.TIE).all().delete()

        return Response(data={'status': u'清除成功'}, status=HTTP_200_OK)
