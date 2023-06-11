from django.contrib import admin

from .models import BlogInfo, Category, TagInfo


@admin.register(BlogInfo)  # 把文章表注册到后面
class ArticleInfoAdmin(admin.ModelAdmin):
    # 展示的字段
    list_display = ['title', 'click_num', 'message_num', 'author', 'category', 'taginfo', 'add_time']
    # 可以搜索
    search_fields = ['title', 'content']


@admin.register(TagInfo)
class TagInfoAdmin(admin.ModelAdmin):
    # 展示的字段
    list_display = ['name', 'category', 'add_time']
    # 可以搜索
    search_fields = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # 展示的字段
    list_display = ['name', 'add_time']
    # 可以搜索
    search_fields = ['name']
