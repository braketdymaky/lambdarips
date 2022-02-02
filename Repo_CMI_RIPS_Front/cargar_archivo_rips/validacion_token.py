import requests
from requests.auth import HTTPDigestAuth
import json

''' la url a continuacion debe cambiar por la del portal
    solo que para no afectar el desarrollo actual esta bajo esta url
    cualquier duda contactar con Fernando Caceres
'''

# url = 'http://3.222.147.86:8081/api/validacionToken/'

# url real
url = 'http://10.0.246.144:8081/api/validacionToken/'


def check(token, cliente, prestador):
    head = {'Authorization': '{}'.format(token), 'cliente': '{}'.format(cliente), 'prestador': '{}'.format(prestador)}
    response = requests.post(url, headers=head)
    data = response.json()
    return data
