from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime
# Create your views here.

def hello(request):
    return HttpResponse('hello world')

def current_datetime(request):
    now =datetime.datetime.now()
    return render_to_response('dateapp/current_datetime.html',{'current_date':now})

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return  HttpResponse(html)