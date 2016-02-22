# --coding: utf-8--
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from api.v1.account.serializers import StudentSignupSerializer, HrSignupSerializer, PasswordChangeSerializer


class StudentSignupAPIView(CreateModelMixin, GenericAPIView):
    serializer_class = StudentSignupSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, **kwargs)


class HrSignupAPIView(CreateModelMixin, GenericAPIView):
    serializer_class = HrSignupSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, **kwargs)


class PasswordChangeAPIView(GenericAPIView):
    serializer_class = PasswordChangeSerializer

    def post(self, request, *args, **kwargs):
        """
        ---
        parameters:
            - name: Authorization
              required: True
              paramType: header
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

