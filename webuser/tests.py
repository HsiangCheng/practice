# --coding: utf-8--
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser

from api.v1.serializers import StudentSerializer


# Create your tests here.
def Test_StudentSerializer(str):
    stream = BytesIO(str)
    data = JSONParser().parse(stream)
    student = StudentSerializer(data=data)
    student.is_valid()
    student.save()