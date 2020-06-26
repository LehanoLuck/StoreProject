from django.conf.urls import url
from cloathesStore import views

app_name = 'cloathesStore'

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<filter>[-\w]+)/(?P<slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_param'),
    url(r'^(?P<id>\d+)/$',
        views.product_detail,
        name='product_detail'),
]