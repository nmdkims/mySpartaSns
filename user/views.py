from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
# Create your views here.
# user/views.py
from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import get_user_model  # 사용자가 데이터 베이스에 있는지 확인하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        if password != password2:
            return render(request, 'user/signup.html')
        else:

            exist_user = get_user_model().objects.filter(username=username)

            if exist_user:
                return render(request, 'user/signup.html')  # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
            else:
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in')


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)

        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return redirect('/sin-in')

    elif request.method == 'GET':

        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
