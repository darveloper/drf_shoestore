from django.shortcuts import render
from rest_framework import viewsets 
from api.models import Manufacturer, ShoeType, ShoeColor, Shoe
from api.serializers import UserSerializer, ShoeTypeSerializer, ShoeColorSerializer, ShoeSerializer

def index(request):
    return render(request, 'index.html', {'shoes': Shoe.objects.all()})


class UserViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = UserSerializer

class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer

class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer

class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer