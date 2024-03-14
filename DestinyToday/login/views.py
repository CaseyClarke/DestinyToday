from django.http import HttpResponse
import requests

def index(request):
    
    HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}
    DATA = { 'grant_type':'authorization_code', 'code': request.GET.urlencode().strip("code=")}
    AUTH = ('46455', 'API_SECRET_KEY_NO_NO_SHARING')


    response = requests.post('https://www.bungie.net/platform/app/oauth/token/', data=DATA, auth=AUTH, headers=HEADERS)
    content = response.content

    jContent = response.json()

    name = requests.get("https://www.bungie.net/platform/User/GetBungieNetUserById/" + jContent["membership_id"], headers= {"X-API-Key" : "37bafe595e9e44f1828f148dd236551c"})

    return HttpResponse(name)
