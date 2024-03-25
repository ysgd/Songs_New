# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Artist(models.Model):
  ArtistName = models.CharField(max_length=50)
  
  def __str__(self):
    return self.ArtistName

class Genre(models.Model):
  GenreName = models.CharField(max_length=50)
  
  def __str__(self):
    return self.GenreName
  
class Album(models.Model):
  AlbumName = models.CharField(max_length=50) 
  AlbumCover = models.ImageField(upload_to="Images")
  
  def __str__(self):
    return self.AlbumName
  
class User(AbstractUser):
  username = models.CharField(max_length=40, unique=True)
  password = models.CharField()
  email = models.EmailField(unique=True)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

class Song(models.Model):
  SongName = models.CharField(max_length=50)
  SongMedia = models.FileField(upload_to="Sounds",null=True)
  SongGenre = models.ManyToManyField(Genre)
  SongArtist = models.ManyToManyField(Artist)
  SongAlbum = models.ForeignKey(Album, on_delete=models.SET_NULL,null=True, related_name='song_album')
  Description = models.TextField()
  CreatedBy = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, related_name='song_creator')
  CreatedOn = models.DateTimeField(auto_now_add=True)
  ModifiedBy = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, related_name='song_modifier')
  ModifiedOn = models.DateTimeField(auto_now=True)
  DeletedBy = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=True, related_name='song_deleter')
  DeletedOn = models.DateTimeField(null=True, blank=True, auto_now=False)
  
  def __str__(self):
    return self.SongName
  
  
