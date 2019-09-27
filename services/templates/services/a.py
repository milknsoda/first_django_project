import requests

response = requests.get('https://artii.herokuapp.com/make?text=name&font=starwars')
print(response.text)