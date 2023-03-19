from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating')
    list_filter = ('dateCreation', 'postCategory')
    search_fields = ('title', 'postCategory')


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
