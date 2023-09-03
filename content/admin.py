from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Content

# Register your models here.
class ContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand', 'category', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Content, ContentAdmin)
