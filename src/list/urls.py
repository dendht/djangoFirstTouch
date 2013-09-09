from django.conf.urls import patterns, include, url

from list import views as list_views

urlpatterns = patterns('',

                       (r'^$',  list_views.PriceShow.as_view()),

                      )