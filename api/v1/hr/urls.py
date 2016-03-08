# --coding: utf-8--

from django.conf.urls import url
from api.v1.hr.views import HrDetailAPIView, HrTargetListAPIView, HrTargetDetailAPIView

urlpatterns = [
    url(r'^info/(?P<username>[\w.@+-]+)/$', HrDetailAPIView.as_view(), name='hr-detail'),
    url(r'^targets/$', HrTargetListAPIView.as_view()),
    url(r'^targets/(?P<pk>[\d.@+-]+)/$', HrTargetDetailAPIView.as_view())
]