from django.shortcuts import render
from django.views.generic import DetailView,ListView
from.models import Product
# Create your views here.
class listview(ListView):
    template_name = 'product/listview.html'
    model = Product
    context_object_name = 'products'
class detailview(DetailView):
    template_name = 'product/detailview.html'
    model = Product
    context_object_name = 'products'