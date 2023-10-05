from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Customer, Queries
from .serializers import CustomerSerializer, QueriesSerializer

from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def home(request): 
    if request.method == 'POST':
        # Process the form data here
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        flight = request.POST.get('flight')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        infants = request.POST.get('infants')
        destination = request.POST.get('destination')
        departure = request.POST.get('departure')
        date_of_travel = request.POST.get('date_of_travel')

        # add to database 
        # Create Customer instance
        customer = Customer.objects.create(name=name, email=email, phone_number=phone, adults=adults, children=children, infants=infants)
        # Create Queries instance
        query = Queries.objects.create(destination=destination, departure=departure, date_of_travel=date_of_travel, customer=customer, flight= flight)


        # Send email
        subject = 'New Travel Query'
        message = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nFlight: {flight}\nDestination: {destination}\nDeparture: {departure}\nAdults: {adults}\nChildren: {children}\nInfants: {infants}\nDate of Travel: {date_of_travel}'
        from_email = 'ahsanmahi019@gmail.com'  # Use the same email as in EMAIL_HOST_USER
        recipient_list = ['tourism.point19@gmail.com']  # Replace with the organization's email address
        
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        # Add a success message to the user's session
        messages.success(request, 'Form submitted successfully!')

        return redirect('thankyou')

    return render(request, 'home.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def tour_details(request):
    return render(request, 'tour-details.html')

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


