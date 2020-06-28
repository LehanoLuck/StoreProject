from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import CreateView
from users.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from cloathesStore.models import Category, Product, Color, Size, UserQuestion, Vacancy
from orders.models import Order, OrderItem
from cart.forms import CartAddProductForm
from .models import CustomUser
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from django.contrib import messages


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


def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__contains=query)
    categories = Category.objects.all()
    colors = Color.objects.all()
    sizes = Size.objects.all()
    return render(request, 'shop/product/list.html',
                  {'categories': categories,
                  'colors': colors,
                  'sizes': sizes,
                  'products': products})


def show_orders(request, id):
    user = CustomUser.objects.get(id=id)
    orders = Order.objects.filter(user_id=user.id)
    order_items = []
    for order in orders:
        items = OrderItem.objects.filter(order_id=order.id)
        order_items.append({'order': order, 'items': items})
    return render(request, 'personal_area.html', {'order_items': order_items})


def show_products(request):
    products = Product.objects.all()
    return render(request, 'Home_DressShop.html', {'products': products})


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


def edit_user(request, id):
    user = CustomUser.objects.get(id=id)
    if request.method == "POST":
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.username = request.POST.get("username")
        user.city = request.POST.get("city")
        user.street = request.POST.get("street")
        user.house = request.POST.get("house")
        user.email = request.POST.get("email")
        user.save()
        return redirect("http://localhost:8000")
    else:
        return render(request, 'edit_area.html')


def send_question(request, id):
    user = CustomUser.objects.get(id=id)
    if request.method == "POST":
        send_mail('Subject here',
                  request.POST.get("message"),
                  'alex.shiro.1024@gmail.com',
                  ['alex.shiro.1024@gmail.com'],
                  fail_silently=True)
        UserQuestion.objects.create(
            message=request.POST.get("message"),
            user_id=id,
            email=user.email
        )
        return redirect("http://localhost:8000")
    else:
        return render(request, 'answer.html')


def send_vacancy(request, id):
    user = CustomUser.objects.get(id=id)
    if request.method == "POST":
        #myfile = request.FILES['myfile']
        #fs = FileSystemStorage()
        #filename = fs.save(myfile.name, myfile)
        #uploaded_file_url = fs.url(filename)
        Vacancy.objects.create(
            position=request.POST.get("position"),
            city=request.POST.get("city"),
            citizenship=request.POST.get("citizenship"),
            #file=myfile,
            user_id=user.id
        )
        messages.info(request, 'Успешно отправлено')
        return redirect("http://localhost:8000")
    else:
        return render(request, 'answer.html')