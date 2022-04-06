from operator import le
from urllib import request
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics, status, filters
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView, get_object_or_404

from core.models import Seller
from core.serializers import SellerSerializer


class SellerViewSet(ModelViewSet):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()


