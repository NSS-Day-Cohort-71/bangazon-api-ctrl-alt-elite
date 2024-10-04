from django.shortcuts import render
from ...models import Order


def unpaid_orders_report(request):
    status = request.GET.get("status")
    if status == "incomplete":
        orders = Order.objects.filter(payment_type=None)
        order_data = []

        for order in orders:
            total_cost = sum(item.product.price for item in order.lineitems.all())
            customer_name = order.customer.user.username
            order_data.append(
                {
                    "id": order.id,
                    "total_cost": total_cost,
                    "customer": customer_name,
                }
            )
        report_data = {"orders": order_data, "name": "Unpaid Orders Report"}
        # more logic
        return render(
            request, "reports/unpaid_order_report.html", {"report_data": report_data}
        )
    # Handle other cases or return an error
