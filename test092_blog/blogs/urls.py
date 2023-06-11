from django.urls import path
from blogs import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog_list/<str:kind>', views.blog_list, name='blog_list'),
    path('blog_detail/<int:id>', views.blog_detail, name='blog_detail'),
    path('blog_search', views.blog_search, name='blog_search'),
]
