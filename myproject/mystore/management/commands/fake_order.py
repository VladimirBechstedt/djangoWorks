from django.core.management.base import BaseCommand
from mystore.models import Order, User, Product
from random import randint


class Command(BaseCommand):
    help = "Print 'Hello world!' to output."

    def handle(self, *args, **kwargs):
        user = User.objects.get(pk=1)
        orders = Order.objects.filter(customer=1)
        for order in orders:
            # product = []
            # price = 0
            # for j in range(randint(1, 5)):
            #     p = Product.objects.get(pk=randint(1, 10))
            #     price += p.price
            #     product.append(p)
            # order = Order(customer=user, total_price=price)
            # order.save()
            # order.products.add(*product)

            # orders = Order.objects.filter(customer=1)
            if order is not None:
                price = 0
                product = []
                for j in range(randint(1, 5)):
                    p = Product.objects.get(pk=randint(1, 10))
                    price += p.price
                    product.append(p)
                order.total_price = price
                order.save()
                order.products.add(*product)
