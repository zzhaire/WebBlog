# WebBlog

使用django搭建的博客系统,具有富文本编辑功能和评论功能

【博客演示视频】 https://www.bilibili.com/video/BV1XX4y1p7kt/?share_source=copy_web&vd_source=ffec7b7c1c2dc2b525e0362c2befce9d

说明:

在 test092_blog 里面的setting里面,把数据库配置成为自己的本地数据库


邮箱注册码我使用的163的,喜欢的可以用自己的,一毛钱就可以开通使用,非常便宜


要用到pillow包和Django框架没有的自己pip install 一下吧


test092_blog在终端中打开

```cmd
python manage.py makemigrations
生成数据库迁移文件
python manage.py migrate
使用迁移文件构建数据库
python manage.py createsuperuser
创建超级管理员完成后,在路由后面+/admin就可以进入网页后台添加文章了
python manage.py runserver
运行服务,如果是本地端口默认是127.0.0.(你配置的端口)
如果是服务器,请在数据库那部分改成你自己的端口

如果有不懂的可以联系我
```

觉着有用的,点个星星吧~
