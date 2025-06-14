from song.models import Author, Song
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    '''
    content = str()
    content += '<ul>'
    for author in Author.objects.all():
        content += f'<li>{author.name}<ul>'
        for song in author.song_set.all():
            content += f'<li>{song.name}</li>'

        content += '</ul>'
        content += '</li>'
    content += '</ul>'

    return HttpResponse(content)
    '''
    context = {
        'author_list' : Author.objects.all()
    }
    return render(request, 'song/index.html', context)

def author(request, author_id):
    '''
    author = Author.objects.filter(id=author_id).first()
    if author is None:
        content = f'Error! id : {author_id} not found'
    else:
        content = f'Author name {author.name}</br>'
        content += f'Birth Date {author.birth_date.strftime("%d/%m/%Y")}</br>'

    return HttpResponse(content)
    '''

    content = {
            'author' : Author.objects.filter(id=author_id).first()
        }
    
    return render(request, 'song/author.html', content)

def song(request):
    '''
    song_id = request.GET.get('song_id')
    song = Song.objects.filter(id=song_id).first()
    if song is None:
        content = f'Error! id : {song_id}'
    else:
        content = f'song name : {song.name}'
    return HttpResponse(content)
    '''
    content = {
            'song':Song.objects.filter(id=request.GET.get('song_id')).first()
        }
    return render(request, 'song/song.html',content)
