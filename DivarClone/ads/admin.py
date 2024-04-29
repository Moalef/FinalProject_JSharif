from django.contrib import admin
<<<<<<< HEAD
from .models import Ad

# Register your models here.
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['title' , 'owner' , 'city' , 'description', 
                    'category', 'contact' , 'publish' , 'status']
    list_filter = ['owner' , 'city', 'category', 'status']
    search_fields = ['title' , 'body']
    #raw_id_fields = ['owner']
    date_hierarchy = 'publish'
    ordering = ['status' , 'publish']
=======
from .models import Ad, Category
# Register your models here.
admin.site.register(Ad)
admin.site.register(Category)
>>>>>>> 36af7f61ffdcae1f28ee2c3a6cede69a7c8f7e72
