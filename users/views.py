from random import Random

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.http import HttpResponse, Http404
from django.views.generic.base import View
from django.db.models import Q
from django.core.mail import send_mail

from .forms import RegisterForm, LoginForm, FindForm, ResetForm
from .models import User
from users.models import Verifycode
from OJ.private_settings import DEFAULT_FROM_EMAIL


# 重定向
def users(request):
    return redirect('users:profile')


# 用户认证模块
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(email=username) | Q(username=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 登录模块
class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active == False:
                    return render(request, 'users/login.html', {'msg': "该账号未激活", 'error': True})
                else:
                    login(request, user)
                    return redirect('index')
            else:
                return render(request, 'users/login.html', {'msg': "用户名或密码错误", 'error': True})
        else:
            return render(request, 'users/login.html', {'msg': "用户名或密码非法", 'error': True})


# 注册模块
class RegisterView(View):

    def get(self, request):
        return render(request, 'users/register.html')

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data['email']
            username = register_form.cleaned_data['username']
            if not User.objects.filter(Q(email=email) | Q(username=username)).exists():
                password_first = register_form.cleaned_data['password_first']
                password_second = register_form.cleaned_data['password_second']
                if password_first == password_second:
                    user = User(username=username, email=email)
                    user.set_password(password_first)
                    user.is_active = False
                    Email(email, 'active')
                    user.save()
                    return render(request, 'users/active.html', {'msg': '注册成功，请在您的邮箱点击链接来激活您的账号', 'from_active': True})
                else:
                    return render(request, 'users/register.html', {'msg': '两次密码不一致', 'error': True})
            else:
                return render(request, 'users/register.html', {'msg': '该用户名或邮箱已存在', 'error': True})
        else:
            return render(request, 'users/register.html', {'msg': "输入的用户名或密码非法", 'error': True})


class resetpasswordView(View):

    def get(self, request, verify_code=''):
        if len(verify_code) == 48:
            if Verifycode.objects.filter(code=verify_code).exists():
                return render(request, 'users/reset.html', {'msg': '请重置你的密码', 'authed': True})
            else:
                raise Http404
        else:
            return render(request, 'users/reset.html')

    def post(self, request, verify_code=''):
        find_form = FindForm(request.POST)
        reset_form = ResetForm(request.POST)
        if find_form.is_valid():
            query = User.objects.filter(username=find_form.cleaned_data['username'])
            if query.filter(email=find_form.cleaned_data['email']).exists():
                Email(find_form.cleaned_data['email'], 'find')
                return render(request, 'users/reset.html', {'msg': '请前往您的邮箱点击链接来修改您的密码', 'submitted': True})
            else:
                return render(request, 'users/reset.html', {'msg': '用户名或邮箱不存在', 'error2': True})
        elif reset_form.is_valid():
            email = reset_form.cleaned_data['email']
            passwordfirst = reset_form.cleaned_data['password_first']
            passwordsecond = reset_form.cleaned_data['password_second']
            destemail = Verifycode.objects.filter(email=email)
            if destemail.filter(code=verify_code).exists():
                if passwordfirst == passwordsecond:
                    user = User.objects.get(email=email)
                    user.set_password(passwordfirst)
                    user.save()
                    destemail.delete()
                    return render(request, 'users/reset.html', {'msg': '重设密码成功', 'success': True, 'authed': True})
                else:
                    return render(request, 'users/reset.html', {'msg': '两次密码不一致', 'error1': True, 'authed': True})
            else:
                return render(request, 'users/reset.html', {'msg': '邮箱错误', 'error1': True, 'authed': True})
        else:
            return render(request, 'users/reset.html', {'msg': '邮箱错误', 'error1': True, 'authed': True})


# 激活账号模块
class activeView(View):
    def get(self, request, verify_code=''):
        if len(verify_code) == 48:
            if Verifycode.objects.filter(code=verify_code).exists():
                destemail = Verifycode.objects.get(code=verify_code)
                user = User.objects.get(email=destemail.email)
                user.is_active = True
                user.save()
                destemail.delete()
                return render(request, 'users/active.html', {'msg': '账号已激活', 'actived': True})
            else:
                raise Http404
        else:
            raise Http404


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


# TODO:完成个人中心页面
class ProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'users/profile.html', {'user': request.user})
        else:
            return redirect('users:login')


# 发送邮件
class Email:
    HOST = 'http://127.0.0.1:8000/'

    def __init__(self, email_address, send_type):
        self.email_addrss = email_address
        if send_type == 'active':
            self.subject = '激活你的账号'
            self.code = self.get_code(email_address)
            active_link = self.HOST + 'users/active/' + self.code
            self.message = '请点击下面的链接 ' + active_link + ' 来激活您的账号'
            send_mail(self.subject, self.message, DEFAULT_FROM_EMAIL, [email_address])
        if send_type == 'find':
            self.subject = '重设你的账号的密码'
            self.code = self.get_code(email_address, 'reset')
            reset_link = self.HOST + 'users/reset/' + self.code
            self.message = '请点击下面的链接 ' + reset_link + ' 来重设您的账号密码，如果不是您的操作，请无视这一封邮件'
            send_mail(self.subject, self.message, DEFAULT_FROM_EMAIL, [email_address])

    def generate_random_code(self, strlength=6):
        result = ''
        origin = 'QAZWSXEDCRFVTGBYHNUJMIKOPqazxswedcvfrtgbnhyujikopl1234567890'
        length = len(origin) - 1
        random = Random()
        for i in range(strlength):
            result += origin[random.randint(0, length)]
        return result

    def get_code(self, email, send_type='active'):
        email_Verify_code = Verifycode()
        random_code = self.generate_random_code(48)
        email_Verify_code.email = email
        email_Verify_code.code = random_code
        email_Verify_code.send_type = send_type
        email_Verify_code.save()
        return random_code
