from marissa.celery_app import app
import json
# from .models import Product
import clothing
from .signals import products_added

@app.task(name='add_to_db')
def add_to_db(items):

    for item in items:
        opt = dict(json.loads(item['options']))
        item['colors_list'] = [option.get('label') for option in opt.get('attributes').get('92').get('options')]
        item['sizes_list'] = [option.get('label') for option in opt.get('attributes').get('183').get('options')]

    products = [
        clothing.models.Product(
            url = item['url'],
            name = item['name'],
            image = item['image'],
            brand = item['brand'],
            price = item['price'].strip(),
            colors = ', '.join(item['colors_list']),
            sizes = ', '.join(item['sizes_list']),
            description = '\n'.join(item['description']),
            category = item['url'].split("/")[-2]
        )
        for item in items
    ]
    clothing.models.Product.objects.bulk_create(products)
    products_added.send(sender=clothing.models.Product)
    return True
