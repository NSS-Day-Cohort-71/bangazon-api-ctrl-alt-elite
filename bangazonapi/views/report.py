from django.shortcuts import render
from bangazonapi.models import Order, Customer


def complete_orders_report(request):

    status = request.GET.get("status", None)

    if status == "complete":
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

    return render(request, 'reports/no_orders.html', {})