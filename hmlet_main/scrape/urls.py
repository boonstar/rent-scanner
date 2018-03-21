from django.conf.urls import url
from scrape import views


app_name = 'scrape'
urlpatterns = [
    url(r'^$', views.SearchView.as_view(), name='question'),
    url(r'^results/(?P<pk>[0-9]+)$', views.ResultView.as_view(), name='results'),
]
