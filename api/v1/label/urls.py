# --coding: utf-8
from django.conf.urls import url

from api.v1.label.views import LabelListAPIView

urlpatterns = [
    url(r'^$', LabelListAPIView.as_view()),
]