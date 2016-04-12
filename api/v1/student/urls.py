# --coding: utf-8--

from django.conf.urls import url
from api.v1.student.views import StudentDetailAPIView, StudentLabelAPIView, StudentLabelDeleteAPIView, \
    StudentInvitationListAPIView, StudentInvitationDetailAPIView, QuestionnaireAPIView, TIEReplyAPIView, \
    TIEReplyCleanAPIView

urlpatterns = [
    url(r'^info/(?P<username>[\w.@+-]+)/$', StudentDetailAPIView.as_view()),
    url(r'^label/$', StudentLabelAPIView.as_view()),
    url(r'^label/(?P<label_id>[\d.@+-]+)/$', StudentLabelDeleteAPIView.as_view()),
    url(r'^invitations/$', StudentInvitationListAPIView.as_view()),
    url(r'^invitations/(?P<pk>[\d.@+-]+)/$', StudentInvitationDetailAPIView.as_view()),
    url(r'^questionnaire/$', QuestionnaireAPIView.as_view()),
    url(r'^questionnaire-reply/$', TIEReplyAPIView.as_view()),
    url(r'^clean-reply/$', TIEReplyCleanAPIView.as_view()),
]