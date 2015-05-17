from django.conf.urls import url
from house import views
urlpatterns = [
    url(r'^$', views.IndexTemplateView.as_view(), name='index'),
]
