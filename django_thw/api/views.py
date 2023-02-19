from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def getRoutes(request):
    
    routes = [
        {
            'Endpoint': '/cards/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of cards being used.'
        },

        {
            'Endpoint': '/cards/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single card object'
        },
    ]
    
    return JsonResponse(routes, safe=False)