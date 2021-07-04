from django_filters import rest_framework as filters

from .models import Item, Category

class ItemFilter(filters.FilterSet):

    class Meta:
        model = Item
        fields = (
            "name" : ["icontains"],
            "category_name" : ["icontains"],
            "category_id" : ["exact"]
        )      

class CategoryFilter(filters.FilterSet):
            