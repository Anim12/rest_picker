from django.conf.urls import url, include
from django.views.generic import ListView
from restaurants.models import Food
from django.conf import settings
from . import views, apps
from django.views.static import serve

urlpatterns = (
    url(r'^$',
        ListView.as_view(
            model=Food,
            template_name='index.html'),
        name='index'),
    url(r'^food/(?P<food_id>\d+)/$', views.choose_city, name='choose_city'),
    url(r'^food/(?P<food_id>\d+)/city/(?P<city_id>\d+)/$', views.choose_restaurant, name='choose_restaurant'),
    url(r'^rest/(?P<rest_id>\d+)/$', views.restaurant, name='restaurant'),
    url(r'^(?P<rest_id>\d+)/vote/$', views.vote, name='vote'),
)

'''if settings.DEBUG:
    urlpatterns += (
         url(r'^media/(?P.*)$',
          serve,
         {'document_root': settings.MEDIA_ROOT}))
'''
