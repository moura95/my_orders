# Create your views here.
from rest_framework import request
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Seller, Company, Portage, Customer, Factory, Employer, Product, Factory_Product, Order, \
    OrderItems, Plan
from core.serializers import SellerSerializer, CompanySerializer, PortageSerializer, CustomerSerializer, \
    FactorySerializer, EmployerSerializer, ProductSerializer, Factory_ProductSerializer, OrderSerializer, \
    OrderItemsSerializer, PlanSerializer


class SellerViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()


class CompanyViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class PortageViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = PortageSerializer
    queryset = Portage.objects.all()


class CustomerViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class FactoryViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated)

    serializer_class = FactorySerializer
    queryset = Factory.objects.all()


class EmployerViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()


class ProductViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class Factory_ProductViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = Factory_ProductSerializer
    queryset = Factory_Product.objects.all()


class OrderViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderItemsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = OrderItemsSerializer
    queryset = OrderItems.objects.all()


class PlanViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PlanSerializer
    # queryset = Plan.objects.all()


    def list(self, request, *args, **kwargs):
        print(request.user)
        queryset = Plan.objects.filter(user=request.user)
        serializer = PlanSerializer(queryset, many=True)
        return Response(serializer.data)
