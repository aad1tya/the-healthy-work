from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Card
from .serializers import CardSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    
    #These are API endpoints
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
    
    return Response(routes)

@api_view(['GET'])
def getCards(request):
    cards = Card.objects.all()
    serializer = CardSerializer(cards, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCard(request, pk):
    card = Card.objects.get(id=pk)
    serializer = CardSerializer(card, many=False)
    return Response(serializer.data)