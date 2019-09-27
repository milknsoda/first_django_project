import requests

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'services/index.html')

def artii(request):
    return render(request, 'services/artii.html')

def artii_result(request):
    name = request.GET.get('name')
    fontname = request.GET.get('fontname')
    url = 'http://artii.herokuapp.com/make?text={}&font={}'.format(name,fontname)
    response = requests.get(url)
    context = {
        'response': response.text
    }
    return render(request, 'services/artii_result.html', context)