from django.shortcuts import render, get_object_or_404
from .models import User, Order
from datetime import datetime, timedelta

import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def main(request):
    logger.info('main page accessed')
    return render(request, "mystore/main.html")


def about_me(request):
    logger.info('about_me page accessed')
    return render(request, "mystore/about.html")


def orders(request, pk, day):
    d = datetime.today() - timedelta(days=day)

    users = User.objects.get(pk=1)
    orders = Order.objects.filter(customer=users, date_order__gt=d)

    context = {'orders': orders}
    logger.info('orders page accessed')
    return render(request, "mystore/orders.html", context)


def order(request, order_pk):
    order = Order.objects.get(pk=order_pk)
    products = order.products.all()
    context = {'products': products,
               'total_price': order.total_price,
               'date': order.date_order}
    logger.info('orders page accessed')
    return render(request, "mystore/product.html", context)
