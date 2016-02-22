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

# class StudentRootView(APIView):
#     def get(self, request, *args, **kwargs):
#         data = {
#             'student-detail':
#                 reverse(
#                     'api:v1:student:student-detail',
#                     request=request,
#                     kwargs={'username': '--username--'}
#                 ),
#         }
#         return Response(data)

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
        parameters:
            - name: Authorization
              paramType: header
              type: string
              required: True
            - name: resume
              paramType: form


        """
        return self.partial_update(request)



