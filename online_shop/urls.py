from django.urls import path
from online_shop import views

urlpatterns = [
    path('product-list/', views.product_list, name='product_list'),
    path('comment/', views.product_comment, name='product_comment'),
    # path('order/', views.product_order, name='product_order'),
    # path('categories/', views.product_category, name='categories'),
    path('product-detail/<int:product_id>/', views.product_detail, name='product_detail')
]


