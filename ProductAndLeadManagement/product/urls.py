from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('leads/', LeadCreateView.as_view(), name='lead-create'),
    path('users/', UserProfileCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserProfileDeleteView.as_view(), name='user-delete'),
    path('reports/leads/<str:start_date>/<str:end_date>/', LeadsBetweenDatesView.as_view(), name='leads-between-dates'),
    path('reports/top-products/', TopProductsView.as_view(), name='top-products'),
    path('reports/bottom-products/', BottomProductsView.as_view(), name='bottom-products'),
    path('reports/leads/products-count/', LeadProductCountView.as_view(), name='leads-products-count'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]