# Create your views here.
from django.contrib.auth.hashers import make_password
from rest_framework import request
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from core.models import Seller, Company, Product, Order, OrderItem, Plan
from core.serializers import SellerSerializer, CompanySerializer, ProductSerializer, OrderSerializer, \
    OrderItemsSerializer, PlanSerializer, UserSerializer, CreateUserSerializer


class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        user_id = request.session.get('_auth_user_id')
        if user_id:
            queryset = User.objects.filter(id=user_id)
        else:
            queryset = User.objects.filter(id=request.user)

        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    # just admin user create new users
    def create(self, request, *args, **kwargs):
        is_staff = request.user.is_staff
        if is_staff:
            password = make_password(request.data["password"])
            request.data["password"] = password
            serializer = CreateUserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class SellerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()

    def get_queryset(self):
        queryset = Seller.objects.filter(user_id=self.request.user)
        return queryset

    def list(self, request, *args, **kwargs):
        user_id = request.session.get('_auth_user_id')
        if user_id:
            queryset = Seller.objects.filter(user_id=user_id)
        else:
            queryset = Seller.objects.filter(user_id=request.user)

        serializer = SellerSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user_id = request.session.get('_auth_user_id')
        if user_id:
            request.data['user'] = user_id
        else:
            request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        user_id = request.session.get('_auth_user_id')
        if user_id:
            request.data['user'] = user_id
        else:
            request.data['user'] = request.user.id
        return super().update(request, *args, **kwargs)


class CompanyViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def get_queryset(self):
        queryset = Company.objects.filter(user_id=self.request.user)
        return queryset

    def list(self, request, *args, **kwargs):
        user_id = request.session.get('_auth_user_id')
        if user_id:
            queryset = Company.objects.filter(user_id=user_id)
        else:
            queryset = Company.objects.filter(user_id=request.user)

        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user_id = request.session.get('_auth_user_id')
        if user_id:
            request.data['user'] = user_id
        else:
            request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)


class ProductViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderItemsViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = OrderItemsSerializer
    queryset = OrderItem.objects.all()


class PlanViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()

    # def list(self, request, *args, **kwargs):
    #     queryset = Plan.objects.filter(user=request.user)
    #     serializer = PlanSerializer(queryset, many=True)
    #     return Response(serializer.data)
