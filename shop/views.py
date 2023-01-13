from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic.edit import CreateView

from .models import Product, Purchase
from .queries import product_data


# Create your views here.
def index(request):
    products = Product.objects.raw(product_data)

    context = {'products': products}
    return render(request, 'shop/index.html', context)


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address']

    def get(self, request, *args, **kwargs):
        product_id = request.resolver_match.kwargs['product_id']
        product = Product.objects.get(id=product_id)

        if product.purchase_set.count() >= product.initial_amount:
            return HttpResponseBadRequest(f'Данного товара нет в наличии'
                                          f'<br><a href="/">На главную</a>')

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        obj: Purchase = form.save(commit=False)

        if obj.product.purchase_set.count() >= obj.product.initial_amount:
            return HttpResponseBadRequest(f'Данного товара нет в наличии'
                                          f'<br><a href="/">На главную</a>')

        obj.save()

        return HttpResponse(f'Спасибо за покупку, {obj.person}!'
                            f'<br><a href="/">На главную</a>')

