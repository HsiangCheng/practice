# --coding: utf-8--
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from api.v1.permissions import IsHrOrReadOnly
from api.v1.recruit.serializers import RecruitSerializer
from webuser.models import Hr, RecruitInfo


class RecruitListAPIView(CreateModelMixin, ListModelMixin, GenericAPIView):
    serializer_class = RecruitSerializer
    queryset = RecruitInfo.objects.all()
    permission_classes = (IsHrOrReadOnly, )

    def get(self, request):
        return self.list(request)

    def post(self, request):
        """
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


