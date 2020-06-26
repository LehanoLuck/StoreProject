from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import CreateView
from users.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from cloathesStore.models import Category, Product, Color, Size
from cart.forms import CartAddProductForm


class HomePageView(TemplateView):
    template_name = 'Home_DressShop.html'


class VacancyView(TemplateView):
    template_name = 'vacancy.html'


class AnswerView(TemplateView):
    template_name = 'answer.html'


class EditAreaView(TemplateView):
    template_name = 'edit_area.html'


class PersonalAreaView(TemplateView):
    template_name = 'personal_area.html'


class InfoView(TemplateView):
    template_name = 'info.html'


class CatalogView(TemplateView):
    template_name = 'catalog.html'


class CartView(TemplateView):
    template_name = 'cart.html'


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def logout_request(request):
    logout(request)
    return redirect("Home_DressShop.html")


def product_list(request, filter=None, slug=None):
    category = None
    color = None
    size = None
    categories = Category.objects.all()
    colors = Color.objects.all()
    sizes = Size.objects.all()
    products = Product.objects.all()
    if slug:
        if filter=='category':
            category = get_object_or_404(Category, slug=slug)
            products = products.filter(category=category)
        elif filter=='color':
            color = get_object_or_404(Color, slug=slug)
            products = products.filter(color=color)
        elif filter=='size':
            size = get_object_or_404(Size, slug=slug)
            products = products.filter(size=size)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'color': color,
                   'size': size,
                   'categories': categories,
                   'colors': colors,
                   'sizes': sizes,
                   'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product,
                                id=id)
    color = get_object_or_404(Color, id=product.color_id)
    size = get_object_or_404(Size, id=product.size_id)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'color': color,
                                                        'size': size,
                                                        'cart_product_form': cart_product_form})
