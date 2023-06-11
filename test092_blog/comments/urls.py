from django.urls import path
from . import views

urlpatterns = [
    path('comment/<int:id>', views.comment, name='comment'),
]
