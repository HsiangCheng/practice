# --coding: utf-8--

from django.conf.urls import url
from api.v1.student.views import StudentDetailAPIView

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', StudentDetailAPIView.as_view()),
]