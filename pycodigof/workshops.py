import requests

def unreleased():
    """Retorna los próximos talleres en CódigoFacilito.
    
    >>> type(unreleased()) == type(dict())
    True
    """

    response = requests.get('https://codigofacilito.com/api/v2/workshops/unreleased')

    if response.status_code == 200:
        payload = response.json()
        return payload['data']

def all():
    """Retorna todos los talleres de CódigoFacilito.
    
    >>> type(all()) == type(list())
    True
    """
    response = requests.get('https://codigofacilito.com/api/v2/workshops')

    if response.status_code == 200:
        payload = response.json()
        return payload['data']