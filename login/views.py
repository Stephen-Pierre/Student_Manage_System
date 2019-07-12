from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = request.POST.get('username')
        pwd = request.POST.get('pwd')
        # print(user, pwd)
        if user == 'root' and pwd == '123123':
            # 登录成功
            return render(request, 'index.html', {'user': user})
        else:
            # 登陆失败
            return render(request, 'login.html', {'msg': "用户名或密码错误!!"})

