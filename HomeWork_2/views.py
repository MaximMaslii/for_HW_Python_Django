from django.shortcuts import render, get_object_or_404, redirect
from .models import Client,Product,Order


def read_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})


def create_client(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        client = Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)
        return redirect('client_detail', client_id=client.id)


def update_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        client.name = request.POST.get('name')
        client.email = request.POST.get('email')
        client.phone_number = request.POST.get('phone_number')
        client.address = request.POST.get('address')
        client.save()
        return redirect('client_detail', client_id=client.id)
    return render(request, 'update_client.html', {'client': client})


def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client.delete()
    return redirect('read_clients')


def read_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def create_product(request):
    if request.method == 'POST':
        return redirect('product_detail', product_id=product.id)


def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        return redirect('product_detail', product_id=product.id)
    return render(request, 'update_product.html', {'product': product})


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('read_products')


def read_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})


def create_order(request, client_id, order=None):
    client = Client.objects.get(pk=client_id)
    if request.method == 'POST':
        return redirect('order_detail', order_id=order.id)
    return render(request, 'create_order.html', {'client': client})


def update_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        return redirect('order_detail', order_id=order.id)
    return render(request, 'update_order.html', {'order': order})


def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    return redirect('read_orders')


def base(request):
    return render(request, 'base.html')