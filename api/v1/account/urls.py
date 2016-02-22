# --coding: utf-8--

from django.conf.urls import url, include
from api.v1.account.views import StudentSignupAPIView, HrSignupAPIView, PasswordChangeAPIView
from api.v1.views import AuthTokenView

urlpatterns = [
    # url(r'^$', AccountRootView.as_view(), name='account-root'),
    url(r'^signup/student/$', StudentSignupAPIView.as_view(), name='student-signup'),
    url(r'^signup/hr/$', HrSignupAPIView.as_view(), name='hr-signup'),
    url(r'^password/change/$', PasswordChangeAPIView.as_view(), name='password-change'),
    url(r'^token-auth/$', AuthTokenView.as_view(), name='auth-token'),
]