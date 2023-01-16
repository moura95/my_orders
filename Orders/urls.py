"""Orders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import SellerViewSet, CompanyViewSet, ProductViewSet, OrderViewSet, OrderItemsViewSet, PlanViewSet, \
    UserViewSet

router = routers.DefaultRouter()

router.register(r"api/seller", SellerViewSet, basename="seller")
router.register(r'api/user-detail', UserViewSet, basename='user-detail')
router.register(r"api/plan", PlanViewSet, basename="plan")
router.register(r"api/company", CompanyViewSet, basename="company")
router.register(r"api/product", ProductViewSet, basename="product")
router.register(r"api/order", OrderViewSet, basename="order")
router.register(r"api/order_items", OrderItemsViewSet, basename="order_items")

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("", include(router.urls)),
    path('openapi', get_schema_view(
        title="My Orders API",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),

]
