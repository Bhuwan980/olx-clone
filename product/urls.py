from django.urls import path
from . import views
urlpatterns = [
    path('product/',views.listview.as_view(),name='listview'),
    path('product/<slug:slug>',views.detailview.as_view(),name='detailview'),
]
