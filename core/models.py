from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

import uuid


# Create your models here.




class category(models.Model):
        
        name = models.CharField(max_length=50)
        slug = models.SlugField(unique=True, max_length=50)
    

        class Meta:
                verbose_name = ("category")
                verbose_name_plural = ("categories")

        def __str__(self):
                return self.name

        def get_absolute_url(self):
                return reverse("category_detail", kwargs={"pk": self.pk})


class product(models.Model):
        product_name = models.CharField( max_length=20)
        slug = models.SlugField(unique=True)
        P_amount = models.DecimalField(max_digits=5, decimal_places=2)
        p_description = models.TextField(blank=True)
        P_image = models.ImageField( upload_to='product_images', height_field=None, width_field=None, max_length=None)
        
        
        
        
        def __str__(self):
                return self.product_name

        class Meta:
                db_table = ''
                managed = True
                verbose_name = 'product'
                verbose_name_plural = 'products'










                
                
class profile(models.Model):
        id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
        
        photo = models.ImageField( upload_to='profile_images', height_field=None, width_field=None, max_length=None)
        balance = models.DecimalField( max_digits=5, decimal_places=2)
        country = models.CharField(max_length=50)
        

        def __str__(self):
                return self.countrypy

        class Meta:
                db_table = ''
                managed = True
                verbose_name = 'profile'
                verbose_name_plural = 'profiles'