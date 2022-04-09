# Create your views here.
from rest_framework.viewsets import ModelViewSet

from core.models import Seller, Company
from core.serializers import SellerSerializer, CompanySerializer


class SellerViewSet(ModelViewSet):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
