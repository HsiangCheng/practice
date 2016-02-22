# --coding: utf-8--

from django.conf.urls import url
from api.v1.hr.views import HrDetailAPIView

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', HrDetailAPIView.as_view(), name='hr-detail'),
]