from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots.txt', TemplateView.as_view(template_name='robots.txt')),
    url(r'^humans.txt', TemplateView.as_view(template_name='humans.txt')),
    url(r'^crossdomain.xml', TemplateView.as_view(template_name='crossdomain.xml')),
    # This is your base URL:
    url(r'^$', TemplateView.as_view(template_name='base.html')),
)
