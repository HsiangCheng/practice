# --coding: utf-8--
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest, QueryDict
from django.views.generic import ListView, TemplateView, FormView, View
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from webuser.forms import LoginForm
from webuser.permissions import *
from webuser.serializers import *
from rest_framework.decorators import api_view, detail_route, list_route
# Create your views here.
import json, urllib

class TestViewSet(ListModelMixin ,RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Student.objects.get_queryset()
    serializer_class = StudentSerializer
    permission_classes = (IsUserPermissions, )

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Student.objects.filter(user_id=user_id)
        return queryset

    # support "PATCH" method
    def partial_update(self, request, *args, **kwargs):
        print "success"
        return Response({"success": "11"})



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.get_queryset()
    serializer_class = StudentSerializer
    permission_classes = (IsUserPermissions, )
    # lookup_field = "username"


    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Student.objects.filter(user_id=user_id)
        return queryset

    @detail_route(methods=['get'])
    def set_password(self, request, pk=None):
        return Response({"success": "detail_route  get"})

    @list_route(methods=['get'])
    def setpassword(self, request):
        return Response({"success": "list_route  get"})

class HrViewSet(viewsets.ModelViewSet):
    queryset = Hr.objects.get_queryset()
    serializer_class = HrSerializer
    permission_classes = (IsUserPermissions,)

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Hr.objects.filter(user_id=user_id)
        return queryset

@api_view(['GET', 'POST'])
def debug(request):
    print u"URL:", request.get_full_path()
    body = request.body
    print u"请求的body：", body
    print u"译码后的body", urllib.unquote(body)
    print u"json化后的body", json.dumps(body)
    # return HttpResponse(json.dumps(body), content_type='application/json')
    res = {}
    res['data'] = body
    response = JsonResponse(res, safe=False)
    print u"响应中的body", response.content
    return response
    # user =  request.data.get('user')
    # username = user.get('username')
    # return HttpResponse(username)

def con_debug():
    str = 'user=%7B%22username%22%3A%225454545%22%2C%22password%22%3A%225555%22%2C%22email%22%3A%225455%22%7D'
    # json_res = json.loads(str)
    Q_dict = QueryDict(str)
    print Q_dict


class HrLoginView(FormView):
    template_name = 'webuser/login.html'
    form_class = LoginForm
    success_url = '/success/'


@login_required(login_url='/login/')
def success(request):
    return render(request, 'webuser/success.html')