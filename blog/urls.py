from django.urls import path
from .views import post_detail , post_list , about, feedback_list

urlpatterns = [
    path('', post_list, name='post_list'),
    path('about/', about, name='about'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('feedback/', feedback_list, name='feedback_list'),

]
