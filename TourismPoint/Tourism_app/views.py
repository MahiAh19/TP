from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Customer, Queries
from .serializers import CustomerSerializer, QueriesSerializer

# Create your views here.
def home(request): 
    return render(request, 'home.html')

@api_view(['GET'])
def customer_list(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_query(request, query_id):
    try:
        query = Queries.objects.get(pk=query_id)
    except Queries.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = QueriesSerializer(query)
    return Response(serializer.data)


