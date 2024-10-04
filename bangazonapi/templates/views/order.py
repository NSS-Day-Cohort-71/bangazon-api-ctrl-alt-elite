from django.shortcuts import render
from ...models import Order


def orders_report(request):
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
    else:
        orders = Order.objects.filter(payment_type__isnull=False)

        report_data = []
        for order in orders:
            report_data.append({
                'order_id': order.id,
                'customer_name': f"{order.customer.user.first_name} {order.customer.user.last_name}",
                'total': sum(item.product.price for item in order.lineitems.all()),
                'payment_type': order.payment_type.merchant_name,
            })

        return render(request, 'reports/complete_orders.html', {'orders': report_data})