from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from bomber.api_views import BomberViewSet
from places.api_views import PlaceViewSet
from labels.api_views import LabelViewSet
from crew.api_views import PersonViewSet

from autocomplete_light import shortcuts as al
al.autodiscover()


router = routers.DefaultRouter()
router.register(r'bombers', BomberViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'labels', LabelViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('webpage.urls', namespace='webpage')),
    url(r'places/', include('places.urls', namespace='places')),
    url(r'labels/', include('labels.urls', namespace='labels')),
    url(r'bombers/', include('bomber.urls', namespace='bombers')),
    url(r'crew/', include('crew.urls', namespace='crew')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
]
