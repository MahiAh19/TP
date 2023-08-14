from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customer_list/', views.customer_list, name='customer-list'),
    path('get_query/<int:query_id>/', views.get_query, name='get-query'),
    path('thankyou', views.thankyou, name='thankyou'),
]