from django.urls import path
from online_shop import views

urlpatterns = [
    path('index/', views.product_list, name='product_list'),
    path('detail/', views.product_detail, name='product_detail'),
    path('comment/', views.product_comment, name='product_comment'),
    path('order/', views.product_order, name='product_order'),

]
