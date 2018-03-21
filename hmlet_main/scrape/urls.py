from django.conf.urls import url
from django.views.generic import TemplateView
from scrape import views


app_name = 'scrape'
urlpatterns = [
    url(r'^$', views.SearchView.as_view(), name='question'),
    url(r'^results/$', TemplateView.as_view(template_name="results.html"), name='results'),
]
