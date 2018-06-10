from django.conf.urls import url
from django.contrib import admin
from core import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'raft_monitoring.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^create_new_node/', views.create_new_node),
    url(r'^node_stoped/', views.node_stoped),
    url(r'^log_read/', views.log_read),
    url(r'^log_write/', views.log_write),
    url(r'^servers_list/', views.servers_list),
    url(r'^server/(?P<pk>\d+)/$', views.server_info, name='server_info'),
]
