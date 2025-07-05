from song import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('author/<int:author_id>', views.author),
    path('song/', views.song),
    path('author_list2/', views.AuthorList.as_view()),
    path('author_list/', views.author_list, name='author_list'),
    path('author_with_song_list/', views.author_with_song_list, name='author_with_song_list'),
    path('song_list', views.song_list),
    path('song_detail/<int:song_id>', views.song_detail),
    path('author_with_song_list2/', views.AuthorWithSongList.as_view())
]

