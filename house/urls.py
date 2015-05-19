from django.conf.urls import url
from django.views.generic.base import TemplateView
from house import views
urlpatterns = [
    url(r'^$', views.ClientInfoListTemplateView.as_view(), name='client_list'),
    url(r'^(?P<client_info_id>[0-9]+)/$', views.ClientDetailTemplateView.as_view(), name='client_detail'),
    url(r'^floorplan/$', TemplateView.as_view(template_name='floor_plan.html'), name="floorplan"),
]

