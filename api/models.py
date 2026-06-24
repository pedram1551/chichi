from django.db import models


class Store(models.Model):
    STORE_TYPES = [
        ('clothes', 'لباس'),
        ('electronics', 'لوازم الکترونیکی'),
        ('home', 'لوازم خانگی'),
        ('food', 'مواد غذایی'),
        ('other', 'سایر'),
    ]

    name = models.CharField(max_length=200)
    store_type = models.CharField(max_length=50, choices=STORE_TYPES)
    description = models.TextField()
    address = models.TextField()
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='products'
    )

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    stock = models.IntegerField(default=1)

    image = models.ImageField(
        upload_to='ads/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name