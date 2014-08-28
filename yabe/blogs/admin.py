from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'created', 'updated')
    list_filter = ('author',)
    search_fields = ('title', 'content',)


admin.site.register(Post, PostAdmin)
