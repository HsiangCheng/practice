# --coding: utf-8--

from django.conf.urls import url
from api.v1.resume.views import ResumeListAPIView, ResumeDetailAPIView

urlpatterns = [
    url(r'^$', ResumeListAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$', ResumeDetailAPIView.as_view()),
]