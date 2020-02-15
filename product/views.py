from django.shortcuts import render
from django.views.generic import DetailView,ListView
from.models import Product,Category
# Create your views here.
class listview(ListView):
    template_name = 'product/listview.html'
    model = Product 
    context_object_name ='products'
    paginate_by = 10
    def get_context_data(self,**kwargs):
        context = super(listview, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

class detailview(DetailView):
    template_name = 'product/detailview.html'
    model = Product
    context_object_name = 'products'
    # queryset = Product.objects.all()       

    # def get_context_data(self,**kwargs):
    #     context = super(detailview, self).get_context_data(**kwargs)
    #     context['category'] = Category.objects.all()
    #     return context