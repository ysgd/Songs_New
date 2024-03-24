from django.contrib import admin
from .models import Song, Artist, Genre, Album, User

admin.site.register(User)

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Song)


