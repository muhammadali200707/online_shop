from django.urls import path
from online_shop import views

urlpatterns = [
    path('product-list/', views.product_list, name='product_list'),
    path('comment/', views.product_comment, name='product_comment'),
    path('product-detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/<int:category_id>/', views.product_list, name='category_detail_id'),
    path('product/<int:product_id>/add-comment', views.add_comment, name='add_comment'),
    path('product/<int:product_id>/add-order', views.add_order, name='add_order'),
    # path('order/', views.product_order, name='product_order'),

]
