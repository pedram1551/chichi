from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Store, Product
from .serializers import StoreSerializer, ProductSerializer


# 🏠 صفحه اصلی سایت
def home(request):
    return HttpResponse("""
    <html>
    <head>
        <title>چی‌چی</title>
    </head>

    <body style="margin:0; font-family:Arial; background:#f5f5f5;">

        <div style="
            text-align:center;
            padding:50px;
            background:linear-gradient(135deg,#ff6b6b,#4ecdc4);
            color:white;
        ">

            <img src="/static/images/Chichi_Logo.png" width="150" style="border-radius:20px;">

            <h1 style="margin-top:20px;">🛍️ چی‌چی</h1>
            <p>به دنیای خرید و فروش خوش اومدی</p>

        </div>

        <div style="padding:20px; text-align:center;">
            <h2>✨ سایت در حال ساخت هست</h2>
            <p>به زودی فروشگاه‌ها و محصولات اینجا نمایش داده میشن</p>
        </div>

    </body>
    </html>
    """)


# 🏪 لیست فروشگاه‌ها (API)
@api_view(['GET'])
def store_list(request):
    stores = Store.objects.all()
    serializer = StoreSerializer(stores, many=True)
    return Response(serializer.data)


# 📦 لیست محصولات (API)
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)