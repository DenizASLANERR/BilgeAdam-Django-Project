from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from product.models import Product
from .models import Cart
from django.views.decorators.csrf import csrf_exempt

# Sepete ürün ekleme
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart:view_cart')

# Sepet görüntüleme
@login_required

def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    cart_total = sum(item.total_price() for item in cart_items)
    return render(request, 'pages/cart.html', {'cart_items': cart_items, 'cart_total': cart_total})

# Ürün adedi güncelleme
@csrf_exempt
@login_required
def update_quantity(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get("product_id")
        quantity = data.get("quantity")

        cart_item = Cart.objects.filter(user=request.user, product_id=product_id).first()
        if cart_item:
            cart_item.quantity = quantity
            cart_item.save()
            product_total = cart_item.total_price()
            cart_total = calculate_cart_total(request.user)

            return JsonResponse({
                "success": True,
                "product_total": product_total,
                "cart_total": cart_total
            })

    return JsonResponse({"success": False}, status=400)

# Ürün silme
@csrf_exempt
@login_required
def remove_item(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get("product_id")

        cart_item = Cart.objects.filter(user=request.user, product_id=product_id).first()
        if cart_item:
            cart_item.delete()

        cart_total = calculate_cart_total(request.user)
        return JsonResponse({"success": True, "cart_total": cart_total})

    return JsonResponse({"success": False})


# Siparişi tamamlama
@csrf_exempt
@login_required
def complete_order(request):
    if request.method == 'POST':
        cart_items = Cart.objects.filter(user=request.user)
        for item in cart_items:
            item.product.stock -= item.quantity
            item.product.save()
            item.delete()

        return JsonResponse({"success": True})

    return JsonResponse({"success": False})


# Sepet toplam hesaplama
def calculate_cart_total(user):
    cart_items = Cart.objects.filter(user=user)
    return sum(item.total_price() for item in cart_items)
