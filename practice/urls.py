# --coding: utf-8--
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
from django.contrib.auth.views import login, logout

from api.v1.routers import SingleRouter
from api.v1.views import AuthTokenView
from webuser.views import *
from webuser.forms import LoginForm

router = routers.DefaultRouter()
router.register(r'test', TestViewSet, "test")
router.register(r'student', StudentViewSet)
router.register(r'hr', HrViewSet)

test_router = SingleRouter()
test_router.register(r'test', TestViewSet, "test")




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'practice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', APIRootView.as_view()),
    # url(r'^', include(router.urls)),
    # url(r'^test/', include(test_router.urls)),
    # url(r'^new-hr/(?P<username>[\w.@+-]+)/$', HrAPIView.as_view()),
    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^docs2/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^debug/$', debug),
    # url(r'^login/$', HrLoginView.as_view(), name='hr-login'),
    url(r'^login/$', login, {'authentication_form': LoginForm, }),
    url(r'^logout/$', logout, {'next_page': '/login/'}),
    url(r'^success/$', success),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
