from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import patterns, include, url
from myproject.views import *
from django.conf.urls.defaults import patterns, include, url
from myproject.views import *
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import *
import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^search/$',search),
    url(r'new/$',new),
    url(r'form/$',form),
    url(r'hello/$',MyAjaxView),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT } ),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT } ),
    url(r'^qwerty/$',qwerty),
    url(r'^cry/$',donate),
    url(r'start/$',start2),
    url(r'^start3/$',start3),
    url(r'^start4/$',start4),
    url(r'^hacku/$',hacku),
    url(r'^carousel/$',carousel),
    url(r'^try/$',trya),
    url(r'^retweets/$',retweets),
    url(r'^screenname/$',screenname),
    url(r'^hashtag/$',hashtags),
    # Examples:
    # url(r'^$', 'buffalo.views.home', name='home'),
    # url(r'^buffalo/', include('buffalo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
