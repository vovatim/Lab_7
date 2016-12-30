from django.shortcuts import render,redirect, render_to_response
from django.http import HttpResponseRedirect
from django.views import View
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from lab.models import RegisterForm
class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'lab/register2.html', {'errors': '', 'form': form.as_p()})

    def post(self, request):
        form = RegisterForm(request.POST)

        if not form.is_valid():
            return render(request, 'lab/register2.html', {'errors': '', 'form': form.as_p()})

        u = User(username=form.cleaned_data['login'], email=form.cleaned_data['email'],
                 last_name=form.cleaned_data['surname'], first_name=form.cleaned_data['name'])
        u.set_password(form.cleaned_data['password'])
        u.save()
        return redirect('/succ/')
    #def get(self,request):
       # return render(request,'lab/register.html',{'errors':'','login':'','email':'','surname':'','name':''})

    #def post(self, request):
      #   login = request.POST['login']
      #   password = request.POST['password']
      #   password2 = request.POST['password2']
      #   email = request.POST['email']
      #   surname = request.POST['surname']
      #   name = request.POST['name']
      #   errors =[]
      #   if len(login) < 5:
      #      errors.append("Логин короткий")
      #   if len(password) < 8:
      #      errors.append("Пароль короткий")
      #   if password != password2:
       #     errors.append("Пароли не совпадают")
      #   if len(email) < 1 or len(surname) < 1 or len(name) < 1:
      #      errors.append("Все поля должны быть заполнены")
      #   if len(errors) == 0:
       #         usrs = User.objects.filter(username=login)
       #         if len(usrs) > 0:
       #             errors.append("Пользователь с данным логином уже существует")
        #        else:
        #            u = User(username=login, email=email, last_name=surname, first_name=name)
        #            u.set_password(password)
        #            u.save()
       #  if len(errors) > 0:
       #         return render(request, 'lab/register.html', {'errors': mark_safe('<br>'.join(errors)), 'login': login,
                               #                          'email': email, 'surname': surname, 'name': name})
        # return redirect('/login/')
class Login(View):
    def get(self, request):
        return render(request, 'lab/login.html', {'errors': '', 'login': ''})

    def post(self, request):
        log = request.POST['login']
        password = request.POST['password']
        errors = []

        user = authenticate(username=log, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        errors.append('Логин или пароль неверны')
        return render(request, 'lab/login.html', {'errors': mark_safe('<br>'.join(errors)), 'login': login})

@login_required(login_url='/login')
def home(request):
    a = 'You are authenticated'
    return render(request, 'lab/home.html', {'auth': a})

class Logout(View):
    success_url = "/"
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")