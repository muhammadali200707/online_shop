from django.shortcuts import render, redirect

from online_shop.forms import CommentModelForm, OrderModelForm
from online_shop.models import Category, Product, Comment, Order
from django.http import HttpResponse
from typing import Optional
from django.shortcuts import get_object_or_404


def product_list(request, category_id: Optional[int] = None):
    categories = Category.objects.all().order_by('id')
    if category_id:
        products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'online_shop/home.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    comments = Comment.objects.filter(product=product_id, is_provide=True).order_by('-id')
    orders = Order.objects.filter(product=product_id).order_by('-id')
    context = {
        'product': product,
        'comments': comments,
        'orders': orders
    }
    return render(request, 'online_shop/detail.html', context)


def product_comment(request, comment_id):
    try:
        comment = Product.objects.get(id=comment_id)
        return render(request, 'online_shop/detail.html', {'comment': comment})
    except:
        return HttpResponse("Sorry, we couldn't find this product ", status=404)


def product_order(request):
    return render(request, 'online_shop/order.html')


# def add_comment(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         body = request.POST.get('body')
#         comment = Comment(name=name, email=email, body=body)
#         comment.product = product
#         comment.save()
#         return redirect('product_detail', product_id)
#     else:
#         pass
#     return render(request, 'online_shop/detail.html')


def add_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', product_id)
    else:
        form = CommentModelForm
    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'online_shop/detail.html', context)


def add_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('product_detail', product_id)
    else:
        form = OrderModelForm
    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'online_shop/detail.html', context)


