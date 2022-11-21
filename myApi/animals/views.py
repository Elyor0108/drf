from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Animals
from .serializer import AnimalsSerializer


class AnimalsViewSet(ModelViewSet):
    queryset = Animals.objects.all()
    serializer_class = AnimalsSerializer


class BillingRecordsSerializer:
    pass


class LargeResultsSetPagination:
    pass


class BillingRecordsView(generics.ListAPIView):
    queryset = Animals.objects.all()
    serializer_class = BillingRecordsSerializer
    pagination_class = LargeResultsSetPagination