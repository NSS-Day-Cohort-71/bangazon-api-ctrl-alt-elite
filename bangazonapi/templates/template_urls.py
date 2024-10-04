from django.urls import path
from .views import order

urlpatterns = [
    path("orders", order.orders_report, name="orders_report"),
]
