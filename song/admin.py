from django.contrib import admin
from song.models import Author, Song


class SongInline(admin.TabularInline):
    model = Song
    extra = 0 #no extra slot
    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [SongInline]
    search_fields = ['name']
    list_display = ['name', 'birth_date', 'display_birth_date']
    readonly_fields = ['display_song_names'] #display 


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    #raw_id_fields = ['author']
    autocomplete_fields = ['author']
