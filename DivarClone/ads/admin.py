from django.contrib import admin
from .models import Ad, Bookmark

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


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user' , 'ad']
    list_filter = ['user' , 'ad']
    search_fields = ['user' , 'ad']
    #raw_id_fields = ['owner']
    ordering = ['user' , 'ad']



