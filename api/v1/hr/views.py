# --coding: utf-8--
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from api.v1.hr.serializers import HrSerializer
from api.v1.permissions import IsUserPermission, IsHr
from webuser.models import Hr

class HrDetailAPIView(UpdateModelMixin, RetrieveModelMixin, GenericAPIView):
    serializer_class = HrSerializer
    queryset = Hr.objects.all()
    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'
    permission_classes = (IsUserPermission, IsHr, )

    def get(self, request, username):
        """
        ---
        parameters:
            - name: Authorization
              paramType: header
              required: True
              type: string
        """
        return self.retrieve(request)

    def patch(self, request, username):
        """
        ---
        parameters:
            - name: Authorization
              paramType: header
              type: string
              required: True
        """
        return self.partial_update(request)

