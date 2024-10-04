from django.urls import path
from .views import order

urlpatterns = [
    path("orders", order.unpaid_orders_report, name="unpaid_orders_report"),
]
