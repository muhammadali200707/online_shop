from django.shortcuts import render


def product_list(request):
    return render(request, 'online_shop/home.html')


def product_detail(request):
    return render(request, 'online_shop/detail.html')


def product_comment(request):
    return render(request, 'online_shop/comment.html')


def product_order(request):
    return render(request, 'online_shop/order.html')
