from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Composition, CompositionDetail
from .serializers import CompositionSerializer, CompositionDetailSerializer

class CompositionViewSet(viewsets.ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer

class CompositionDetailViewSet(viewsets.ModelViewSet):
    queryset = CompositionDetail.objects.all()
    serializer_class = CompositionDetailSerializer

