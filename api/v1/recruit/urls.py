# --coding: utf-8--

from django.conf.urls import url
from api.v1.recruit.views import RecruitListAPIView, RecruitDetailAPIView

urlpatterns = [
    url(r'^$', RecruitListAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$', RecruitDetailAPIView.as_view()),
]