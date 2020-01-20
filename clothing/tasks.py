from marissa.celery_app import app
import json
# from .models import Product
import clothing
from .signals import products_added

@app.task(name='add_to_db')
def add_to_db(items):
    print(f"WE RECEIVED LIST OF {len(items)} ITEMS")
    for item in items:
        clothing.models.Product.objects.create(
            url = item['url'],
            name = item['name'],
            image = item['image'],
            brand = item['brand'],
            price = item['price'].strip(),
            description = '\n'.join(item['description']),
            category = item['url'].split("/")[-2]
        )
    products_added.send(sender=clothing.models.Product)
    return True
