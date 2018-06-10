from django.conf.urls import url
from django.contrib import admin
from core import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'raft_monitoring.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^create_new_node/', views.create_new_node),
]
