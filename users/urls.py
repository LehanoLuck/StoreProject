from django.urls import path
from cloathesStore import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]