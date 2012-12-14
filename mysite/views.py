#!/usr/bin/env python
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Template,Context
import datetime
def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date':now}))
    #return HttpResponse(html)
    return render_to_response('current_datetime.html',{'current_date':now})

def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now() + datetime.timedelta(hours=offset)
    html= "<html><body>In %s hour(s),it will be %s.</body></html>" %(offset,dt)
    return HttpResponse(html)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

