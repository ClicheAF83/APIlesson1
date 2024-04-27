import requests
from django.shortcuts import render

def home(request):
  #USING APIs
  response = requests.get('https://api.github.com/users/naveenkumar-s')
  data = response.json()
  result = data['id']

  #example2
  response2 = requests.get('https://dog.ceo/api/breeds/image/random')
  data2 = response2.json()
  result2 = data2['message']
                           

  
  return render(request, 'templates/index.html', {'result': result, 'result2': result2})