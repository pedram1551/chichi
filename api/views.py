from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Store, Product
from .serializers import StoreSerializer, ProductSerializer


# صفحه اصلی
def home(request):
    products = Product.objects.all().order_by('-id')

    return render(
        request,
        'home.html',
        {
            'products': products
        }
    )


# لیست فروشگاه‌ها (API)
@api_view(['GET'])
def store_list(request):
    stores = Store.objects.all()
    serializer = StoreSerializer(stores, many=True)
    return Response(serializer.data)


# لیست محصولات (API)
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

