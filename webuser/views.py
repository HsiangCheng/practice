# --coding: utf-8--
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest, QueryDict
from rest_framework import viewsets
from webuser.permissions import *
from webuser.serializers import *
from rest_framework.decorators import api_view
# Create your views here.
import json, urllib

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.get_queryset()
    serializer_class = StudentSerializer
    permission_classes = (IsUserPermissions, )

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Student.objects.filter(user_id=user_id)
        return queryset

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