# Logic for getting favorite seller data
from django.shortcuts import render
from ...models import Customer, Favorite
from django.contrib.auth.models import User
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.response import Response


def favorite_seller_report(request):
    customer_id = request.GET.get("customer")
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist as ex:
        return render(
            request, "reports/favorite_seller_report.html", {"None": "Does Not exist"}
        )

    user = User.objects.get(pk=customer.user_id)
    favorites = Favorite.objects.filter(customer=customer)

    favorite_sellers = []
    for favorite in favorites:
        seller = Customer.objects.get(pk=favorite.seller_id)
        favorite_sellers.append(User.objects.get(pk=seller.user_id))
    report_data = {"customer": user, "favorite_sellers": favorite_sellers}

    return render(
        request, "reports/favorite_seller_report.html", {"report_data": report_data}
    )
