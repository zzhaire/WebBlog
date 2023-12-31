from django.urls import path
from users import views

urlpatterns = [
    path('user_register', views.user_register, name='user_register'),
    path('user_login', views.user_login, name='user_login'),
    path('user_active', views.user_active, name='user_active'),
    path('user_logout', views.user_logout, name="user_logout"),
]
