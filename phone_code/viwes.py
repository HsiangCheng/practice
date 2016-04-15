# --coding: utf-8--
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from phone_code.models import PhoneCode


class PhoneCodeAPIView(GenericAPIView):
    def get(self, request, phone):
        """
        获取手机验证码
        ---
        parameters:
            - name: phone
              required: True
              paramType: path
              description: 获取验证码手机号码
        """
        phone_code = PhoneCode.objects.get_or_update_phone_code(phone)
        return Response({'code': phone_code.code, 'timeout': phone_code.timeout})
