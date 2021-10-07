from django.shortcuts import render, HttpResponse, Http404
from MainApp.models import Item

products = [
    {"id": 1, "name": "Кроссовки adidas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 3, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 4, "name": "Картофель фри", "quantity": 0},
    {"id": 5, "name": "Кепка", "quantity": 124},
]

# Create your views here.
# def main(request):
#     name = f"Иванов И.П."
#     html = f"""
#     <h1>"Изучаем django"</h1>
#     <strong>Автор</strong>: <i>{name}</i>
#     """
#
#     return HttpResponse(html)

# def main(request):
#     return render(request, "index.html")

def main(request):
    # context = {
    #     "products": products
    # }
    return render(request, "index.html")

def about(request):
    # просто переменная с данными
    user_data = {
        'name': "Руслан",
        'surname': "Кузнецов",
        'patronymic': 'Отчество',
        'phone': '+9200000000',
        'email': 'rkuznetsov@mail.ru'
    }

    html = f"""
    <p>Имя: {user_data["name"]}</p>
    <p>Отчество: {user_data["patronymic"]}</p>
    <p>Фамилия: {user_data["surname"]}</p>
    <p>телефон: {user_data["phone"]}</p>
    <p>email: {user_data["email"]}</p>
    """

    return HttpResponse(html)

def items(request):
    products = Item.objects.all
    context = {
        "products": products
    }
    return render(request, "items.html", context)

# def item(request, id):
#
#     for item in products:
#         if item["id"] == id:
#             return render(request, "item.html", item)
#     raise Http404
# # return HttpResponse(f"Не найден товар с таким ID:{id}.")

def item(request, id):
    try:
        product = Item.objects.get(id = id)
    except Item.DoesNotExist:
        raise Http404
    context = {
        "item": product
    }
    return render(request, "item.html", context)

    # raise Http404