
from importlib import import_module


from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'author', 'created', 'update')
    prepopulated_fields = {"slug" : ('title',)}



# Register your models here.
