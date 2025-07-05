from song.models import Author, Song
from django.http import HttpResponse
from django.shortcuts import render
import json


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

def author_list(request):
    authors = Author.objects.all()
    response_data = list()
    print(request)

    for author in authors:
        author_data = dict()
        author_data['name'] = author.name
        author_data['birth_date'] = author.birth_date.strftime('%d-%m-%y')
        author_data['image'] = author.image.url
        response_data.append(author_data)
    return HttpResponse(json.dumps(response_data))

def song_list(request):
    get_request = request.GET.get('author_id')
    if get_request != None:
        songs = Song.objects.filter(author__id=get_request) if len(get_request) > 0 else ''
        reponse_data = []

        for song in songs:
            song_data = {}
            song_data['name'] = song.name
            reponse_data.append(song_data)

        return HttpResponse(json.dumps(reponse_data))

    else:
        return HttpResponse("Nope", status=400)

def author_with_song_list(request):
    authors = Author.objects.all()
    response_data = list()

    for author in authors:
        author_data = dict()
        author_data['name'] = author.name
        author_data['birth_date'] = author.birth_date.strftime('%d-%m-%y')
        author_data['image'] = author.image.url
        author_data['song_names'] = ", ".join([s.name for s in author.song_set.all()])
        response_data.append(author_data)
    return HttpResponse(json.dumps(response_data)) 

def song_detail(request, song_id):
    song = Song.objects.filter(id=song_id).first()

    song_data = {"name" : song.name,
                 "author_name" : song.author.name
                }

    return HttpResponse(json.dumps(song_data), status=200) if song else HttpResponse('404', status=404)
    
