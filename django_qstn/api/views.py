from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.
def status_view(request):
    print(request)
    return JsonResponse({'message': 'Hello World!'})

def status_html_view(request):
    api_url = 'http://127.0.0.1:8000/status/'
    response = requests.get(api_url)
    message = response.json().get('message', 'Error: Unable to fetch message')
    return render(request, 'api/status.html', {'message': message})