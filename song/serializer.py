from song.models import Author, Song
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format='%d/%m/%Y')
    birth_date_2 = serializers.DateField(source="birth_date", format='%Y-%m-%d', read_only=True)

    length_of_song = serializers.SerializerMethodField()
    songs = serializers.SerializerMethodField()

    def get_length_of_song(self, obj):
        return obj.song_set.all().count()

    def get_songs(self, obj):
        #songs = []
        #for i in obj.song_set.all():
        #    songs.append(i.name)
        #return songs
        return ", ".join([s.name for s in obj.song_set.all()])

    class Meta:
        model = Author
        fields = "__all__"

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"
