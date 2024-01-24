from django.contrib import admin
from .models import category, product, member
# Register your models here.
@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    prepopulated_fields ={'slug':('name',)}




class productAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'P_amount', 'p_description', 'P_image',)
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(product, productAdmin)


class memberAdmin(admin.ModelAdmin):
    list_display = (  'user', 'photo', 'phoneNO', 'country', 'created', )

admin.site.register(member, memberAdmin)
