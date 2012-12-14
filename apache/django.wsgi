#!/usr/bin/env python
mport os
import sys
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
app_apth = "/root/mysite/"
sys.path.append(app_apth)
application = django.core.handlers.wsgi.WSGIHandler()
