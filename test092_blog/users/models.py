from django.contrib.auth.models import AbstractUser  # 使用Django自带的表结构
from django.db import models  # Django 自带的models 引入charField等字段
from datetime import datetime


class UserProfile(AbstractUser):
    """
    1.用户名 : username(唯一) ,用自己编写的:nick_name
    2.密码 : password
    3.邮箱 : email
    4.头像 : image
    5.注册时间 : add_time
    6.激活状态 : is_start
    """
    nick_name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="用户昵称"
    )
    image = models.ImageField(
        upload_to='user/%y/%m/%d',
        verbose_name='头像',
        max_length=200,
        null=True,
        blank=True
    )
    add_time = models.DateTimeField(
        default=datetime.now,
        verbose_name='注册时间'
    )
    is_start = models.BooleanField(
        default=False,
        verbose_name='是否激活'
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'UserProfile'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


class VerifyCodeEmail(models.Model):
    """
    验证表: 用来对用户激活时做处理
    1. email: 用户邮箱
    注意: 使用了图片, 则需要安装pillow模块
    Terminal中输入命令来生成迁移文件
    2. code: 发送给邮箱的验证码
    3. code_type: 邮箱的类型, 可以在注册, 重置等功能中
    4. add_time: 发送验证码的时间, 默认发送的时间
    """
    email = models.EmailField(max_length=30, verbose_name='用户邮箱')
    code = models.CharField(max_length=128, verbose_name='验证码')
    code_type = models.CharField(
        max_length=100,
        choices=(('1', 'register'), ('2', 'reset'), ('3', 'changeemail'), ('4', 'sendpwd')),
        verbose_name='验证码类型'
    )
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'VerifyCodeEmail'
        verbose_name = '验证码信息表'
        verbose_name_plural = verbose_name
