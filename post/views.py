from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import  csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(['POST','GET'])
def hello_django_bbs(request):
    html = "<h1>hello 张二群</h1>"
    # if request.method == 'GET':
    #     html = "<h1>hello 张二群2</h1>"
    return HttpResponse(html)