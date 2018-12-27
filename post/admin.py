from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = [ 'active', 'date']
    list_display = ['title', 'date']
    search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)