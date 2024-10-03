from django.urls import path
from .reports.orders import order

urlpatterns = [
    path("orders", order, name="unpaid_orders_report"),
]
