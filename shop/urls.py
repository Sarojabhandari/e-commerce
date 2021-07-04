from django.urls import path
from .api import category_list


urlpatterns = [ 
    path('categories', category_list)
]
