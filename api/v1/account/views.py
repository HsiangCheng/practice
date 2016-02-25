# --coding: utf-8--
from rest_framework import renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from api.v1.account.serializers import StudentSignupSerializer, HrSignupSerializer, PasswordChangeSerializer


class StudentSignupAPIView(CreateModelMixin, GenericAPIView):
    serializer_class = StudentSignupSerializer

    def post(self, request, *args, **kwargs):
        """
        学生用户注册
        """
        return self.create(request, **kwargs)


class HrSignupAPIView(CreateModelMixin, GenericAPIView):
    serializer_class = HrSignupSerializer

    def post(self, request, *args, **kwargs):
        """
        Hr用户注册（之后的版本可能关闭）
        """
        return self.create(request, **kwargs)


class PasswordChangeAPIView(GenericAPIView):
    serializer_class = PasswordChangeSerializer

    def post(self, request, *args, **kwargs):
        """
        修改密码（需登录）
        ---
        parameters:
            - name: Authorization
              required: True
              paramType: header
              description: 用户的验证令牌，填写格式：Token *********
            - name: password
              paramType: form
              required: True
              type: string
            - name: new_password
              paramType: form
              required: True
              type: string

        """
        if request.user.is_authenticated():
            user = request.user
            password = request.data.get('password', None)
            new_password = request.data.get('new_password', None)
            if not user.check_password(password):
               return Response({'password': 'The password is error.'})
            user.set_password(new_password)
            user.save()
            return Response({'state': 'success'})
        return Response({'user': 'Not login.'})


class AuthTokenView(ObtainAuthToken):
    renderer_classes = (
        renderers.JSONRenderer,
        renderers.BrowsableAPIRenderer,
    )
    def post(self, request, *args, **kwargs):
        """
        获取令牌
        ---
        serializer: rest_framework.authtoken.serializers.AuthTokenSerializer
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        groups = list()
        for group in user.groups.all():
            groups.append(str(group))
        return Response(
            {
                'token': "Token %s" % token.key,
                'username': user.username,
                'groups': groups,
            }
        )