from django.conf.urls import patterns, include, url
from django.contrib import admin
import war_manager.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Warranty_bank_2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls), name = 'admin'),
    url(r'^$', war_manager.views.Home.as_view(), name = 'home'),
    url(r'^loginRedirect/$', war_manager.views.login_redirect, name='login-redirect'),
    url(r'^manage/$', war_manager.views.ManagerHome.as_view(), name='manager-home'),
    url(r'^import/$', war_manager.views.ImportProductView.as_view(), name='importer-home'),
    url(r'^redirect/$', war_manager.views.user_redirect, name='user-redirect'),
    url(r'^receiver/$', war_manager.views.text_receiver, name='text-parser'),
    url(r'^addToDb/$', war_manager.views.addProductToDatabase, name='add-product'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^search/$', war_manager.views.SearchPage, name='search-page'),
    url(r'^viewCustomer/(?P<cust_id>[0-9]+)$', war_manager.views.customerDetail, name='individual-customer-page'),
    url(r'^modelList/$', war_manager.views.ModelList.as_view(), name='model-list'),
    url(r'^modelNew/$', war_manager.views.ModelCreate.as_view(), name='model-create'),
    url(r'^modelEdit/(?P<pk>[0-9]+)$', war_manager.views.ModelUpdate.as_view(), name='model-edit'),    
)

urlpatterns += staticfiles_urlpatterns()