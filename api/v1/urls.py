# --coding: utf-8--

from django.conf.urls import url, include

urlpatterns = [
    url(r'^account/', include('api.v1.account.urls')),
    url(r'^student/', include('api.v1.student.urls')),
    url(r'^hr/', include('api.v1.hr.urls')),
    url(r'^resume/', include('api.v1.resume.urls')),
]
