# Create your views here.
from rest_framework import request
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from core.models import Seller, Company, Product, Order, OrderItem, Plan
from core.serializers import SellerSerializer, CompanySerializer, ProductSerializer, OrderSerializer, \
    OrderItemsSerializer, PlanSerializer


class UserViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = SellerSerializer

    def list(self, request, *args, **kwargs):
        print(request.user)
        queryset = User.objects.filter(user=request.user)
        serializer = PlanSerializer(queryset, many=True)
        return Response(serializer.data)


class SellerViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()


class CompanyViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class ProductViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderItemsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = OrderItemsSerializer
    queryset = OrderItem.objects.all()


class PlanViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PlanSerializer

    def list(self, request, *args, **kwargs):
        queryset = Plan.objects.filter(user=request.user)
        serializer = PlanSerializer(queryset, many=True)
        return Response(serializer.data)
