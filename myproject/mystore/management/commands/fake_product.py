from django.core.management.base import BaseCommand
from mystore.models import Product


class Command(BaseCommand):
    help = "Print 'Hello world!' to output."

    def handle(self, *args, **kwargs):
        for i in range(10):
            product = Product(product_name=f'product{i}', description=f'product description number {i}',
                              price=1000.00 + (i * 10), quantity=i)
            product.save()
