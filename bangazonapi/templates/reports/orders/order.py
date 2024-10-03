from django.shortcuts import render
from ....models import Order


def unpaid_orders_report(request):
    status = request.GET.get("status")
    if status == "incomplete":
        orders = Order.objects.filter(payment_type=False)
        return render(request, "templates/reports/base.html", {"orders": orders})
    # Handle other cases or return an error
