import requests

# AUTH_ENDPOINT can also be https://foursquare.com/oauth2/authenticate
AUTH_ENDPOINT = 'https://foursquare.com/oauth2/authorize'
TOKEN_ENDPOINT = 'https://foursquare.com/oauth2/access_token'
VERSION = '20130128'
API_ENDPOINT = 'https://api.foursquare.com/v2/'

# Set the credentials throught the tuple
cred = ('client_id', 'client_secret', 'redirect_uri')
# The access_token is also accessible
access_token = False

def oauth_url():
    parameters = (AUTH_ENDPOINT, cred[0], cred[2])
    return '{0}?response_type=code&client_id={1}&redirect_uri={2}'.format(*parameters)


def download_token(code):
    global access_token
    params = {
        'client_id': cred[0],
        'client_secret': cred[1],
        'redirect_uri': cred[2],
        'grant_type': 'authorization_code',
        'code': code
    }
    r = requests.get(TOKEN_ENDPOINT, params=params)
    json = r.json()
    
    if 'error' in json:
        raise Exception(json['error'])
     
    access_token = json['access_token'] 
    return access_token

def request(endpoint, params = {} , method = 'GET'):
    global access_token
    params['v'] = VERSION
    if access_token:
        params['oauth_token'] = access_token
    else:
        params['client_id'] = cred[0]
        params['client_secret'] = cred[1]
            
    uri = API_ENDPOINT + endpoint
    
    if method == 'POST':
        r = requests.post(uri, params=params)
    else:
        r = requests.get(uri, params=params)
    json = r.json()
    
    if json['meta']['code'] != 200:
        raise Exception(json['meta']['errorDetail'])

    return json['response']
