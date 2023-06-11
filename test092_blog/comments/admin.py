from django.contrib import admin

# Register your models here.
from .models import Comment


@admin.register(Comment)
class CommentInfoAdmin(admin.ModelAdmin):
    list_display = ['comment_user', 'comment_blog', 'content', 'add_time']
    search_fields = ['comment_user', 'comment_blog', 'add_time']
