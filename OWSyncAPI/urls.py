from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from api_app import views

admin.autodiscover()


# API routs
router = routers.DefaultRouter()
router.register(r'artists', views.ArtistViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OWSyncAPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
)
