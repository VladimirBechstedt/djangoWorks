from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from .models import User, Order, Product
from .forms import ImageForm
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
    return render(request, "mystore/order.html", context)


def product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product,
               'form': ImageForm()}
    return render(request, "mystore/product.html", context)


def upload_image(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']

            # product = Product.objects.get(pk=pk)
            product.image = f'../../../media/{image.name}'

            fs = FileSystemStorage()
            fs.save(image.name, image)

    else:
        form = ImageForm()
    context = {'product': product,
               'form': form}
    return render(request, 'mystore/product.html', context)
