from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order, OrderItem


#create your views here
def product_list(request):
    products = Product.objects.all()

    return render(request, 'pos/product_list.html', {'products' : products})


def create_order(request):
    if request.method == 'POST':
        product_ids = request.POST.getlist('product_ids')
        quantities  = request.POST.getlist('quantities')

        order = Order.objects.create(total = 0)

        for product_id, quantity in zip(product_ids, quantities):
            product = Product.objects.get(id = product_id)

            OrderItem.objects.create(order = order, product = product, quantity = int(quantity))

        return redirect('order_detail', order_id = order.id)
    return redirect('product_list')


def order_detail(request, order_id):
    order = get_object_or_404(Order, id = order_id)

    return render(request, 'pos/order_detail.html', {'order' : order})
