from django.test import TestCase
from .models import Customer, Queries
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime

# Create your tests here.

def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)

class CustomerQueriesTest(TestCase):
    def test_create_customer(self):
        customer = Customer.objects.create(name='John Doe', phone_number='1234567890', email='john@example.com')
        self.assertEqual(customer.name, 'John Doe')
        self.assertEqual(customer.phone_number, '1234567890')
        self.assertEqual(customer.email, 'john@example.com')

    def test_create_query(self):
        customer = Customer.objects.create(name='Jane Doe', phone_number='32145678', email='jane@example.com')
        expected_date = datetime.datetime(2024, 1, 20)  # Convert '20-01-2024' to datetime object
        
        query = Queries.objects.create(destination='Maldives', departure='Dhaka', date_of_travel = expected_date, customer=customer)

        self.assertEqual(query.destination, 'Maldives')
        self.assertEqual(query.departure, 'Dhaka')
        self.assertEqual(query.date_of_travel, expected_date)
        self.assertEqual(query.customer, customer)

    def test_query_does_not_exist(self):
        with self.assertRaises(Queries.DoesNotExist):
            Queries.objects.get(pk=100)  # Assuming 100 is not a valid query ID

    def test_get_query(self):
        customer = Customer.objects.create(name='Alice Johnson', phone_number='5555555555', email='alice@example.com')
        
        expected_date = datetime.datetime(2024, 1, 20) 
        query = Queries.objects.create(destination='London', departure='Los Angeles', date_of_travel = expected_date, customer=customer)
        
        queried_query = Queries.objects.get(pk=query.pk)
        self.assertEqual(queried_query, query)
