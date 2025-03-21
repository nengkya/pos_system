from django.db import models

#create your models here
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)

    total = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)

    def __str__(self):
        return f'Order {self.id}'



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name = 'items', on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def save(self, * args, ** kwargs):
        self.price = self.product.price * self.quantity
        super().save(* args, ** kwargs)

        self.order.total = sum(item.price for item in self.order.item.all())
        self.order.save()
