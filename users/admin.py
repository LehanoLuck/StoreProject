from django.contrib import admin
from cloathesStore.models import UserQuestion,Category,CartItem,Cart,Product, Color, Size
from orders.models import Order, OrderItem
from django.contrib.auth.admin import UserAdmin
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'city', 'street', 'house', 'is_staff',]


admin.site.register(UserQuestion)
admin.site.register(Category)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(OrderItem)
admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
