# Create your views here.
from rest_framework.viewsets import ModelViewSet

from core.models import Seller, Company, Portage, Customer, Factory, Employer, Product, Factory_Product, Order, OrderItems
from core.serializers import SellerSerializer, CompanySerializer, PortageSerializer, CustomerSerializer, FactorySerializer, EmployerSerializer, ProductSerializer, Factory_ProductSerializer, OrderSerializer, OrderItemsSerializer


class SellerViewSet(ModelViewSet):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class PortageViewSet(ModelViewSet):
    serializer_class = PortageSerializer
    queryset = Portage.objects.all()


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class FactoryViewSet(ModelViewSet):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()


class EmployerViewSet(ModelViewSet):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class Factory_ProductViewSet(ModelViewSet):
    serializer_class = Factory_ProductSerializer
    queryset = Factory_Product.objects.all()


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderItemsViewSet(ModelViewSet):
    serializer_class = OrderItemsSerializer
    queryset = OrderItems.objects.all()
