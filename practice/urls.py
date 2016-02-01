# --coding: utf-8--
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views
from webuser.views import *
from django.contrib.auth.views import login, logout
from webuser.forms import LoginForm
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'test', TestViewSet, "test")
router.register(r'student', StudentViewSet, "student")
router.register(r'hr', HrViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'practice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/token-auth/', views.obtain_auth_token),
    url(r'^debug/$', debug),
    # url(r'^login/$', HrLoginView.as_view()),
    url(r'^login/$', login, {'authentication_form': LoginForm, }),
    url(r'^logout/$', logout, {'next_page': '/login/'}),
    url(r'^success/$', success),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
