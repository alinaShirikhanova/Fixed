from django.contrib import admin
from django.urls import path

from trades.views import *

urlpatterns = [
    path('', index, name='index'),
    path('trades/', categories, name='categories'),
    path('categories/<int:category_id>/<int:page>', by_category, name='paginator'),
    path('basket/', basket, name='basket'),
    path('basket/remove/<int:product_id>', basket_min, name='basket_min'),
    path('basket/add/<int:product_id>', basket1, name='add_product'),
]