from django.conf.urls import patterns, url

from wikigraph import views

urlpatterns = patterns('',
                       url(r'^$', views.home, name='home'),
                       url(r'^stats', views.stats, name='stats'),
                       url(r'^(?P<n>\d+)/$', views.home_adv, name='home_advanced'),
                       url(r'^details/(?P<node>.+)/$', views.node_detail, name='node_detail'),
                       url(r'^shortest_path/(?P<node1>.+)/(?P<node2>.+)/', views.shortest_path, name='shortest_path'),
)

