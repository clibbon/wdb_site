from django.conf.urls import patterns, include, url
from django.contrib import admin
import war_manager.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Warranty_bank_2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', war_manager.views.Home.as_view(), name = 'home'),
    url(r'^serviceLogin/$', 'django.contrib.auth.views.login', name = 'service_login'),
    url(r'^goodbye/$', 'django.contrib.auth.views.logout', name = 'logout'),
    url(r'^customerLogin/$', war_manager.views.Placeholder.as_view(),
        name = 'customer_login'),
    url(r'^importerLogin/$', war_manager.views.Placeholder.as_view(),
        name = 'importer_login'),
    url(r'^loginRedirect/$', war_manager.views.login_redirect, name='login-redirect'),
)
