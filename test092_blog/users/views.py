from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.urls import reverse
from .forms import RegisterForm, UserLoginForm
from .models import UserProfile, VerifyCodeEmail
from tools.send_verify_code import send_verify_email


def user_register(request):
    """用户注册"""
    if request.method == "GET":
        return render(request, 'user_register.html')
    else:
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')
            nick_name = register_form.cleaned_data.get('nick_name')

            user = UserProfile.objects.filter(username=email)
            if user:
                return render(request, 'user_register.html', {'msg': '用户名已存在'})
            else:
                user = UserProfile()
                user.email = email
                user.username = email
                user.set_password(password)
                user.nick_name = nick_name
                user.save()
                send_verify_email(email)
            return render(request, 'wait_start.html')
        else:  # 数据错误的提示
            return render(request, 'user_register.html', {'error_tips': register_form})


def user_login(request):
    """用户登录"""
    if request.method == "GET":
        return render(request, "user_login.html")
    else:
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            email = user_login_form.cleaned_data.get('email')
            pwd = user_login_form.cleaned_data.get('password')
            # Django 自带的方法校验账号密码
            user = authenticate(username=email, password=pwd)
            if user:  # 校验正确
                user_obj = UserProfile.objects.get(username=email)
                if user_obj.is_start:
                    login(request, user)
                    return redirect('/')
                else:
                    return render(request, 'user_login.html', {'msg': "请激活账号"})
            else:
                return render(request, 'user_login.html', {'msg': "邮箱和密码错误"})
        else:
            return render(request, 'user_login.html', {'error_tips': user_login_form})


def user_active(request):
    """用户激活"""
    sign = request.GET.get('sign')
    if sign:
        verify_code = VerifyCodeEmail.objects.filter(code=sign)
        if verify_code:
            email = verify_code[0].email
            user_obj = UserProfile.objects.get(email=email)
            user_obj.is_start = True
            user_obj.save()
            verify_code.delete()
            return redirect(reverse('user_login'))  # return redirect('/user_login')
    return render(request, '404.html')


def user_logout(request):
    """用户退出"""
    logout(request)
    return redirect('/')
