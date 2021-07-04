
from django.urls import reverse
from django.db import models
from django.utils.translation import gettext as _
from django.db.models.fields.related import ForeignKey


# Create your models here

LABEL = (
    ('N', 'New'),
    ('BS', 'Best Seller')
)

class Category(models.Model):

    name = models.CharField('Name',max_length=100)
    parent = models.ForeignKey(
    "self",verbose_name=_('Parent'),on_delete= models.SET_NULL, null=True, blank=True)
    image = models.ImageField(('image'), upload_to="categories/", null=True, blank=True)

    

    class Meta:
       verbose_name = _("Category")
    verbose_name_plural = _("Categorys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})
        
        
class Item(models.Model):
        name = models.CharField('Name',max_length=100)
        Category = models.ForeignKey(_("shop.category"), verbose_name=("category"), on_delete=models.CASCADE)
        price = models.FloatField("Price")
        label = models.CharField(_("Label"), choices=LABEL, max_length=50)
        discount_price = models.FloatField(_("Discount-price"),blank=True, null=True)
        despytcription = models.TextField("description")
        image = models.ImageField(('image'), upload_to="categories", null=True, blank=True)

        
    
        class Meta:
            verbose_name = _("Item")
            verbose_name_plural = _("Items")
    
        
    
        def __str__(self):
         return self.name

        def get_absolute_url(self):
            return reverse("Item_detail", kwargs={"pk": self.pk})

