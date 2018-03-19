from django.conf.urls import url
from scrape import views


app_name = 'scrape'
urlpatterns = [
    url(r'^$', views.SearchView.as_view(), name='question'),
]
