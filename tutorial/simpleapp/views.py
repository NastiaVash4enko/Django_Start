from django.views.generic import ListView, DetailView
from .models import Product


class ProductList(ListView):
    model = Product  # указать модель которую мы будем выводить
    template_name = 'products.html'  # указываем имя шаблона, в котором будет лежать html
    context_object_name = 'products'  # это имя списка в которм будут лежа ь все объекты
    queryset = Product.objects.order_by('-id')


# создаём представление, в котором будут детали конкретного отдельного товара
class ProductDetail(DetailView):
    model = Product  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'product.html'  # название шаблона будет product.html
    context_object_name = 'product'  # название объекта. в нём будет
