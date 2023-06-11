from django.core.mail import send_mail
from users.models import VerifyCodeEmail
from test092_blog.settings import EMAIL_FROM
import time
import hashlib  # MD5加密文件


def make_sign():
    """
    时间戳 + test090_blog加密
    :return: sign 加密字符串
    """

    time_sign = str(time.time()) + 'test090_blog'
    md5_sign = hashlib.md5()
    md5_sign.update(time_sign.encode())
    sign = md5_sign.hexdigest()
    return sign


def send_verify_email(to_email):
    """
    发送验证邮件
    为了保证唯一性, 该邮件只能是某一用户的激活邮件, 该邮件后面的参数通过加密来得到一
    个字符串
    """
    sign = make_sign()

    verify_code = VerifyCodeEmail()
    verify_code.email = to_email
    verify_code.code = sign
    verify_code.code_type = 1
    verify_code.save()

    verify_url = '点击链接激活账号\n   http://127.0.0.1:8000/user_active?sign=' + sign

    details = '<p>尊敬的用户您好！</p>' \
              '<p>感谢您使用此网站。</p>' \
              '<p>您的邮箱为：%s 。请点击此链接激活您的邮箱：</p>' \
              '<p><a href="%s">%s<a></p>' \
              % (to_email, verify_url, verify_url)
    # send_mail(subject,'',发件人,[收件人],'邮箱的文本内容)
    subject = '邮箱验证'
    send_mail(subject, '', EMAIL_FROM, [to_email], html_message=details)
