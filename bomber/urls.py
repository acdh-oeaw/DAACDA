from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'list/$', views.bomber, name='bomber_list'),
    url(r'^detail/(?P<pk>[0-9]+)$', views.BomberDetailView.as_view(), name='bomber_detail')
]
