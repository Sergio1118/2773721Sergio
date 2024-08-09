import requests
from bs4 import BeautifulSoup

# URL de la página que quieres analizar
url = 'https://example.com'

# Realiza la solicitud HTTP
response = requests.get(url)

# Verifica que la solicitud fue exitosa
if response.status_code == 200:
    # Analiza el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extrae información específica
    # Por ejemplo, todos los encabezados <h1>
    headers = soup.find_all('h1')
    for header in headers:
        print(header.text)
else:
    print(f"Error al hacer la solicitud: {response.status_code}")