from django.shortcuts import render, redirect
from .models import OrderItem, Order
from cart.cart import Cart
from users.models import CustomUser


def order_create(request, user_id):
    cart = Cart(request)
    user = CustomUser.objects.get(id=user_id)
    order = Order.objects.create(first_name=user.first_name,
                                 last_name=user.last_name,
                                 username=user.username,
                                 email=user.email,
                                 city=user.city,
                                 street=user.street,
                                 house=user.house,
                                 user_id=user_id)
    for item in cart:
        OrderItem.objects.create(order=order,
                                 name=item['product'].name,
                                 product=item['product'],
                                 price=item['price'],
                                 quantity=item['quantity'])
    # очистка корзины
    cart.clear()
    return render(request, 'orders/order/created.html',
                      {'order': order})