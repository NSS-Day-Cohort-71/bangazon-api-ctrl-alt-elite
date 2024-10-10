from django.shortcuts import render
from ...models import Product


def expensive_products_report(request):

    # "gte" = greater than or equal to

    expensive_products = Product.objects.filter(price__gte=1000.00)
    product_data = []

    for product in expensive_products:
        product_data.append(
            {
                "product_id": product.id,
                "name": product.name,
                "price": product.price,
            }
        )
    # products = {"products": product_data, "name": "Products Over $1000"}
    # more logic
    return render(
        request, "reports/expensive_products_report.html", {"products": product_data}
    )
