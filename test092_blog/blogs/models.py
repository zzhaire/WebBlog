from django.db import models
import random
from datetime import datetime
from users.models import UserProfile
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    """博客分类"""
    name = models.CharField(max_length=20, verbose_name='分类名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    is_tab = models.BooleanField(default=True, verbose_name='是否导航')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Category'
        verbose_name = '类别表'
        verbose_name_plural = verbose_name


class TagInfo(models.Model):
    """博客标签"""
    name = models.CharField(max_length=20, verbose_name='标签名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    category = models.ForeignKey(Category, verbose_name='所属分类', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'TagInfo'
        verbose_name = '标签表'
        verbose_name_plural = verbose_name


class BlogInfo(models.Model):
    """博客信息"""
    title = models.CharField(max_length=50, verbose_name='标题')
    introduce = models.TextField(max_length=80, verbose_name='简介')
    content = RichTextUploadingField(verbose_name='文章内容')
    click_num = models.IntegerField(default=0, verbose_name='浏览数')
    message_num = models.IntegerField(default=0, verbose_name='留言数')
    love_num = models.IntegerField(default=0, verbose_name='点赞数')
    cover = models.ImageField(
        upload_to='%y/%m/%d', verbose_name='封面',
        max_length=200,
        default='cover/default' + str(random.choice("12345")) + '.jpg',
        null=True, blank=True
    )
    author = models.ForeignKey(UserProfile, verbose_name='文章作者', on_delete=models.DO_NOTHING)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发表时间')
    is_recommend = models.BooleanField(default=False, verbose_name='首页推荐')
    category = models.ForeignKey(Category, verbose_name='分类表', on_delete=models.DO_NOTHING)
    taginfo = models.ForeignKey(TagInfo, verbose_name='标签表', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "BlogInfo"
        verbose_name = '文章表'
        verbose_name_plural = verbose_name
