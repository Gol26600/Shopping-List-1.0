from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name="home_view"),
    path('edit_product/<str:pk>', edit_product_view, name="edit_product"),
    path('delete_product/<str:pk>', delete_product_view, name="delete_product"),
    path('products/', products_view, name="products"),
    path('notes/', notes_view, name="notes"),
]