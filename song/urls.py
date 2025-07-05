from song import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('author/<int:author_id>', views.author),
    path('song/', views.song),
    path('author_list/', views.author_list)
]

