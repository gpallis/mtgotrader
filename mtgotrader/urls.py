from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^trader/$', 'cardviewer.views.home'),
    url(r'^trader/login/$', 'loginapp.views.loginattempt'),
    url(r'^cardviewer/(?P<card_id>\d+)/$', 'cardviewer.views.detail'),
    url(r'^trader/profile/$', 'loginapp.views.profile'),
    #url(r'^mtgotrader/', include('mtgotrader.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^trader/admin/', include(admin.site.urls)),
)
