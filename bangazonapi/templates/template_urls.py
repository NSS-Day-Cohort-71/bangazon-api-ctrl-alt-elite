from django.urls import path
from .views import expensive_products, favorite_seller, order

urlpatterns = [
    path("orders", order.orders_report, name="orders_report"),
    path(
        "expensiveproducts",
        expensive_products.expensive_products_report,
        name="expensive_products_report",
    ),
    path(
        "favoritesellers",
        favorite_seller.favorite_seller_report,
        name="favorite_seller_report",
    ),
]
