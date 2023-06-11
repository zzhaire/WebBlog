from django.db import models
from datetime import datetime
from blogs.models import BlogInfo
from users.models import UserProfile


# Create your models here.
class Comment(models.Model):
    comment_user = models.ForeignKey(UserProfile, verbose_name='评论人', on_delete=models.DO_NOTHING)
    comment_blog = models.ForeignKey(BlogInfo, verbose_name='评论文章', on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=300, verbose_name='评论内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='评论时间')

    def __str__(self):
        return self.comment_user.email

    class Meta:
        db_table = 'Comment'
        verbose_name = '用户评论信息表'
        verbose_name_plural = verbose_name
