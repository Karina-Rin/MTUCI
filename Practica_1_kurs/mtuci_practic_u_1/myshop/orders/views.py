from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, render

from cart.cart import Cart

from .forms import OrderCreateForm
from .models import Order, OrderItem
from .tasks import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            # очистка корзины
            cart.clear()
            # запуск асинхронной задачи
        order_created.delay(order.id)
        return render(request, "orders/order/created.html", {"order": order})
    else:
        form = OrderCreateForm
    return render(request, "orders/order/create.html", {"cart": cart,
                                                        "form": form})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "admin/orders/order/detail.html", {"order": order})
