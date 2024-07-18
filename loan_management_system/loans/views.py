from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Loan, Payment
from .serializers import LoanSerializer, PaymentSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
