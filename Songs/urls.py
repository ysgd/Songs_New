from django.urls import path
from .views import UserView,GroupView,ArtistView,GenreView,SongView,AlbumView

urlpatterns = [
    path('register/',UserView.as_view({'post':'register'}),name='register'),
    path('login/',UserView.as_view({'post':'login'}),name='login'),
    path('role/',GroupView.as_view({'get':'list'}),name='role'),
    path('artist/',ArtistView.as_view({'get':'list','post':'create'}),name='artist-add'),
    path('artist/<int:pk>/',ArtistView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='artist-update'),
    path('album/',AlbumView.as_view({'get':'list','post':'create'}),name='album-add'),
    path('album/<int:pk>/',AlbumView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='album-update'),
    path('genre/',GenreView.as_view({'get':'list','post':'create'}),name='genre-add'),
    path('genre/<int:pk>/',GenreView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='genre-update'),
    path('song/',SongView.as_view({'get':'list','post':'create'}),name='song-add'),
    path('song/<int:pk>/',SongView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='song-update')
]