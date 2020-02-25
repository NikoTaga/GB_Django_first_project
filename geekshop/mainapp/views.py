from django.shortcuts import render
from .models import ProductCategory, Product
from django.conf import settings


# Create your views here.

def main(request):
    title = 'главная'
    products = Product.objects.all()
    content = {
        'title': title,
        'products': products,
        'media_url': settings.MEDIA_URL
    }
    return render(request, 'mainapp/index.html', content)

def products(request, pk=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()
    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'media_url': settings.MEDIA_URL
    }
    if pk:
        print(f'выбранная категория{pk}')
    return render(request, 'mainapp/products.html', content)

def contact(request):
    title = 'контакты'
    # visit_date = datetime.datetime.now()
    location = [
        {
            'toun': 'Таганрог',
            'fon': '+7-888-888-8888',
            'mail': 'info@geekshop.ru',
            'addr': 'В центре'
        },
        {
            'toun': 'Москва',
            'fon': '+7-888-888-8888',
            'mail': 'info@geekshop.ru',
            'addr': 'В пределах МКАД'
        },
        {
            'toun': 'СПб',
            'fon': '+7-888-888-8888',
            'mail': 'info@geekshop.ru',
            'addr': 'В разумных пределах'
        },
    ]
    content = {'title': title, 'location': location}
    return render(request, 'mainapp/contact.html', content)

