from django.shortcuts import render
import requests

def home(request):
    response = requests.get('https://jsonmock.hackerrank.com/api/movies/search/?Title=spiderman&page=1')
    moviedata = response.json()
    return render(request, 'core/home.html', {
        'data': moviedata['data'],
        'title': moviedata[sorted('title')]
    })