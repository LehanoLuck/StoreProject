"""testStoreProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from cloathesStore.views import HomePageView, VacancyView, AnswerView, PersonalAreaView, EditAreaView, InfoView
from cloathesStore import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.show_products, name='home'),
    path('Home_DressShop.html', views.show_products, name='home'),
    path('vacancy', VacancyView.as_view(), name='vacancy'),
    path('answer', AnswerView.as_view(), name='answer'),
    path('edit_area', EditAreaView.as_view(), name='edit_area'),
    path('info', InfoView.as_view(), name='info'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path("logout", views.logout_request, name="logout"),
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^shop/', include('cloathesStore.urls', namespace='cloathesStore')),
    url(r'^(?P<id>\d+)/$', views.show_orders, name='personal_area'),
    url(r'^edit_area/(?P<id>\d+)/$', views.edit_user, name='edit_user'),
    url(r'^answer/(?P<id>\d+)/$', views.send_question, name='send_question'),
    url(r'^vacancy/(?P<id>\d+)/$', views.send_vacancy, name='send_vacancy'),
    url(r'^vacancy/(?P<id>\d+)/$', views.send_vacancy, name='send_vacancy'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)