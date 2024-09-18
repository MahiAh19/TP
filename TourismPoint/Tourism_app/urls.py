from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer_list/', views.customer_list, name='customer-list'),
    path('get_query/<int:query_id>/', views.get_query, name='get-query'),
    path('thankyou', views.thankyou, name='thankyou'),
    path('tour-details/', views.tour_details, name='tour-details'),
]