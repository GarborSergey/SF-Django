from datetime import datetime
from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Product


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'SimpleApp/products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context


class ProductDetail(DeleteView):
    model = Product
    template_name = 'SimpleApp/product.html'
    context_object_name = 'product'
