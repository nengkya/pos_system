#copy paste and run from python manage.py shell
from pos.models import Product

#list of example products
products_data = [
    {"name": "Laptop", "price": 999.99, "stock": 10},
    {"name": "Coffee", "price": 4.99, "stock": 100},
    {"name": "Smartphone", "price": 599.99, "stock": 25},
    {"name": "Headphones", "price": 149.99, "stock": 50},
    {"name": "Notebook", "price": 2.99, "stock": 200},
    {"name": "Tablet", "price": 299.99, "stock": 30},
    {"name": "Monitor", "price": 199.99, "stock": 15},
    {"name": "Keyboard", "price": 49.99, "stock": 75},
    {"name": "Mouse", "price": 19.99, "stock": 120},
    {"name": "Printer", "price": 129.99, "stock": 20},
]

#create and save products
for data in products_data:
    product = Product(**data)
    product.save()
    print(f"Created: {product.name}")
