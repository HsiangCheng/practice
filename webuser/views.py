# --coding: utf-8--
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse, QueryDict, Http404
from django.views.generic import FormView
from rest_framework.decorators import api_view, detail_route, list_route
from webuser.forms import LoginForm



# Create your views here.
import json, urllib

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
    res['method'] = request.method
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