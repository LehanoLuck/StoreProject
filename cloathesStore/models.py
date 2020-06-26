from django.db import models
from django.urls import reverse
from users.models import CustomUser


class Color(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'color'
        verbose_name_plural = 'colors'
        db_table = 'Color'

    def get_absolute_url(self):
        return reverse('cloathesStore:product_list_by_param', args=['color', self.slug])

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'size'
        verbose_name_plural = 'sizes'
        db_table = 'Size'

    def get_absolute_url(self):
        return reverse('cloathesStore:product_list_by_param', args=['size', self.slug])

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('cloathesStore:product_list_by_param', args=['category', self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='smartphone', blank=True)
    discount = models.FloatField(default=0)
    sex = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        db_table = 'Product'

    def get_absolute_url(self):
        return reverse('cloathesStore:product_detail', args=[self.id])

    def __str__(self):
        return self.name


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product


class UserQuestion(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    adminEmail = models.CharField(max_length=250)
    message = models.CharField(max_length=500)

    class Meta:
        db_table = 'UserQuestion'
