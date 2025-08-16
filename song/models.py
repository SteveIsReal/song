from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    image = models.ImageField(upload_to='media/images', null=True, blank=True)

    @property
    def display_birth_date(self):
        return self.birth_date.strftime("%d / %m / %Y")

    @property
    def display_song_names(self):
        return ' ,'.join([i.name for i in self.song_set.all().order_by('name')])

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/files', null=True)

    def __str__(self):
        return f'{self.author.name} : {self.name}'

