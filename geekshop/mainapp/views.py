from django.shortcuts import render

# Create your views here.

def main(request):
    title = 'главная'
    products = [
        {
            "name": 'Отличный стул',
            "desc": "Расположитесь комфортно.",
            "img_src": "product-1.jpg",
            "img_href": "products/",
            'alt': 'ПРодукт 1'
        },
        {
            "name": 'Стул повышенного качества',
            "desc": "Не оторваться.",
            "img_src": "product-2.jpg",
            "img_href": "products/",
            'alt': 'ПРодукт 2'
        }
    ]
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)

def products(request):
    title = 'продукты'
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    same_products = [
        {
            "name": 'Стул повышенного качества',
            "desc": "Не оторваться.",
            "img_src": "product-11.jpg",
            'alt': 'Продукт 1'
        },
         {
            "name": 'Стул превосходного качества',
            "desc": "Не наглядеться.",
            "img_src": "product-21.jpg",
            'alt': 'Продукт 2'
        },
         {
            "name": 'Стул потрясающего качества',
            "desc": "Не насидеться.",
            "img_src": "product-31.jpg",
            'alt': 'Продукт 3'
        },
    ]
    content = {'title': title, 'links_menu': links_menu, 'same_products': same_products}
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

