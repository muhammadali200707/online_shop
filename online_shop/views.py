from django.shortcuts import render
from online_shop.models import Category, Product
from django.http import HttpResponse


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'online_shop/home.html', context)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        return render(request, 'online_shop/detail.html', {'product': product})
    except:
        return HttpResponse("Sorry, we couldn't find this product ", status=404)


def product_comment(request, comment_id):
    try:
        comment = Product.objects.get(id=comment_id)
        return render(request, 'online_shop/detail.html', {'comment': comment})
    except:
        return HttpResponse("Sorry, we couldn't find this product ", status=404)

# def product_detail(request, pk):
#     product = Product.objects.get(Product, pk=pk)
#     comments = product.comments.all()
#     return render(request, 'online_shop/detail.html', {
#         'product': product,
#         'comments': comments
#     })


def product_order(request):
    return render(request, 'online_shop/order.html')


def product_category(request):
    category = Category.objects.all()
    context = {
        'categories': category
    }
    return render(request, 'online_shop/home.html', context)
