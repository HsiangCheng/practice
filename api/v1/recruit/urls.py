# --coding: utf-8--

from django.conf.urls import url
from api.v1.recruit.views import RecruitListAPIView

urlpatterns = [
    url(r'^$', RecruitListAPIView.as_view()),
]