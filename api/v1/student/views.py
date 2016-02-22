# --coding: utf-8--
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from api.v1.permissions import IsUserPermission, IsStudent
from api.v1.student.serializers import StudentSerializer
from webuser.models import Student

class StudentDetailAPIView(UpdateModelMixin, RetrieveModelMixin, GenericAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'
    permission_classes = (IsUserPermission, IsStudent, )

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
        omit_parameters:
            - form
        parameters:
            - name: Authorization
              paramType: header
              type: string
              required: True
            - name: body
              paramType: body
              type: WriteStudentSerializer

        """
        return self.partial_update(request)



