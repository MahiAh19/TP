from rest_framework import serializers
from .models import Customer, Queries

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone_number', 'email', 'adults', 'children', 'infants']
        read_only_fields = ['id']

class QueriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queries 
        fields = ['id', 'destination', 'departure', 'date_of_travel', 'customer', 'flight']
        read_only_fields = ['id']

        
