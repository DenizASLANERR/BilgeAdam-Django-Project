from django.shortcuts import render, get_object_or_404
from category.models import Category
from product.models import Product


def category(request, category_name):

    category = get_object_or_404(Category, name=category_name)


    categories = [category] + list(category.children.all())

    products = Product.objects.filter(category__in=categories)

    return render(request, 'pages/category.html', {'category_name': category_name, 'products': products})
