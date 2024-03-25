from rest_framework import serializers
from .models import Artist, Genre, Album, Song, User
from django.contrib.auth.models import Group

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ['id','name']

class ArtistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artist
    fields = ('ArtistName',)
    
class GenreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Genre
    fields = ('GenreName',)
    
class AlbumSerializer(serializers.ModelSerializer):
  class Meta:
    model = Album
    fields = ('AlbumName',)
    
class SongSerializer(serializers.ModelSerializer):
  class Meta:
    Album = AlbumSerializer
    Genre = GenreSerializer
    Artist = ArtistSerializer
    model = Song
    fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['email','password','groups']
    