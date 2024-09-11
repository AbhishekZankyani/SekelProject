from django.shortcuts import render
from .models import *
from .serializers import *
from django.db.models import Count
from rest_framework.views import APIView
from django.utils.dateparse import parse_date
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class ProductListCreateView(generics.ListCreateAPIView):
    getAllProducts = Product.objects.all()
    serializer = ProductSerializer
    permission = [IsAuthenticated]

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    getAllProducts = Product.objects.all()
    serializer = ProductSerializer
    permission = [IsAuthenticated]

class LeadCreateView(generics.CreateAPIView):
    leads = Lead.objects.all()
    serializer = LeadSerializer
    permission = []

class UserListCreateView(generics.ListCreateAPIView):
    Users = User.objects.all()
    serializer = UserSerializer
    permission = [IsAuthenticated]

    def perform_create(self, serializer):
        # Hash the password before saving the user
        serializer.save(password=make_password(serializer.validated_data['password']))

class UserDetailView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer = UserSerializer
    permission = [IsAuthenticated]


class UserProfileCreateView(generics.CreateAPIView):
    getAllUsers = UserProfile.objects.all()
    serializer = UserSerializer
    permission = [IsAuthenticated]

class UserProfileDeleteView(generics.DestroyAPIView):
    getAllUsers = UserProfile.objects.all()
    serializer = UserSerializer
    permission = [IsAuthenticated]

class LeadsBetweenDatesView(APIView):
    def get(self, request, startDate, endDate):
        start = parse_date(startDate)
        end = parse_date(endDate)
        leads = Lead.objects.filter(CreatedAt__range=[start, end])
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)

class TopProductsView(APIView):
    def get(self, request):
        products = Product.objects.annotate(leadCount=Count('lead')).order_by('-lead_count')[:10]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class BottomProductsView(APIView):
    def get(self, request):
        products = Product.objects.annotate(leadCount=Count('lead')).order_by('lead_count')[:10]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class LeadProductCountView(APIView):
    def get(self, request):
        leadCounts = Lead.objects.annotate(product_count=Count('products'))
        data = [{"lead": lead.name, "product_count": lead.product_count} for lead in leadCounts]
        return Response(data)

