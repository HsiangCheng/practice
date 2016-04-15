# --coding: utf-8--

from django.conf.urls import url, include

from phone_code.viwes import PhoneCodeAPIView

urlpatterns = [
    url(r'^(?P<phone>[\d]+)/$', PhoneCodeAPIView.as_view()),
]