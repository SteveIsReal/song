from song import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register('author', views.AuthorViewSet)
router.register('song', views.SongViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('author/<int:author_id>', views.author),
    path('song/', include(router.urls)),
    path('author_list2/', views.AuthorList.as_view()),
    path('author_list/', views.author_list, name='author_list'),
    path('author_with_song_list/', views.author_with_song_list, name='author_with_song_list'),
    path('song_list', views.song_list),
    path('song_detail/<int:song_id>', views.song_detail),
    path('author_with_song_list2/', views.AuthorWithSongList.as_view()),
    path('song_list3/', views.SongListGeneric.as_view()),
    path('song_list4/<int:author_id>/', views.SongList4.as_view()),
    path('author_detail/<int:id>', views.AuthorDetail.as_view()),
    path('author_update/<int:id>', views.AuthorUpdate.as_view()),
    path('song_detail2/<str:name>', views.SongDetail.as_view()),
    path('author_create/', views.AuthorCreate.as_view())
]

