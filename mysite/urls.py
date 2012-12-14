from  django.conf.urls.defaults import *
from django.views.generic import list_detail
from books.views import about_pages 
from django.conf import settings
from mysite import views 
from books.models import Publisher 

from django.views.generic.simple import direct_to_template
from django.contrib import admin
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('mysite.views',
    ('^hello/$','hello'),
    ('^time/$','current_datetime'),
    ('^time/plus/(\d{1,2})/$','hours_ahead'),
    ('^meta/$','display_meta'),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

publisher_info = {
        'queryset': Publisher.objects.all(),
        'template_name':'publisher_list_page.html',
        }

urlpatterns += patterns('books.views',
    (r'^search/$','search'),
    (r'^contact/$','contact'),
    (r'^contact/thanks/$','thanks'),
    (r'^about/$',direct_to_template,{'template': 'thanks.html'
        }),
    (r'^publisher/$',list_detail.object_list,publisher_info),
    (r'^about/(w+)/$',about_pages),
    (r'^image/$','my_image'),
    (r'^pdf/$','hello_pdf'),
    )
