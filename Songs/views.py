from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework.viewsets import ModelViewSet
from .serializers import GroupSerializer, UserSerializer, ArtistSerializer, GenreSerializer, AlbumSerializer, SongSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import User, Artist, Genre, Album, Song
from rest_framework.response import Response
# Create your views here.

class GroupView(ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  permission_classes = [AllowAny]
  
class ArtistView(ModelViewSet):
  queryset = Artist.objects.all()
  serializer_class = ArtistSerializer
  permission_classes = [AllowAny]
  
class GenreView(ModelViewSet):
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer
  permission_classes = [AllowAny]
  
class AlbumView(ModelViewSet):
  queryset = Album.objects.all()
  serializer_class = AlbumSerializer
  permission_classes = [AllowAny]
  
class SongView(ModelViewSet):
  queryset = Song.objects.all()
  serializer_class = SongSerializer  
  
class UserView(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny]
  
  def register(self,request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      password = request.data.get('password')
      hash_password = make_password(password)
      a = serializer.save()
      a.password = hash_password
      a.save()
      return Response("User Created")
    else:
      return Response(serializer.errors)
    
  def login(self,request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(username=email,password=password)
    
    if user == None:
      return Response('invalid credentials')
    else:
      token,_= Token.objects.get_or_create(user=user)
      return Response({'token':token.key})
    
