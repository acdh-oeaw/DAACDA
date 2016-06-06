from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'bombers/$', views.BomberListView.as_view(), name='browse_bombers'),
    url(r'persons/$', views.PersonListView.as_view(), name='browse_persons'),
]
