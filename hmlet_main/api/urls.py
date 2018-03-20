from django.conf.urls import url, include
from . import views


apiurls = [
    url(r'^estate/$', views.EstateListAPIView.as_view(), name='estate'),
    url(r'^estate/(?P<pk>[0-9]+)$', views.EstateAPIView.as_view(), name='estate-detail'),
    url(r'^question/$', views.QuestionListAPIView.as_view(), name='question'),
    url(r'^question/(?P<pk>[0-9]+)$', views.QuestionAPIView.as_view(), name='question-detail'),
]

urlpatterns = [
    url(r'^$', views.api_root, name='api-root'),
    url(r'^', include(apiurls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]