from django.urls import path
from .views import store_list, product_list

urlpatterns = [
    path('stores/', store_list),
    path('products/', product_list),
]