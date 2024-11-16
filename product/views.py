from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def products(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "pages/product.html", {"product": product})

def search(request):
    keyword = request.GET.get('keyword', '')
    products = Product.objects.filter(name__icontains=keyword) if keyword else []
    context = {
        'products': products,
        'keyword': keyword,
    }
    return render(request, 'pages/search.html', context)

