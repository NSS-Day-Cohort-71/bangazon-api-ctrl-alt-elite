from django.urls import path
from .views import order
from .views import expensive_products

urlpatterns = [
    path("orders", order.orders_report, name="orders_report"),
    path("expensiveproducts", expensive_products.expensive_products_report, name="expensive_products_report")
]
