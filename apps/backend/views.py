from django.shortcuts import render


def login(request):
    print('ログイン')
    return render(request, 'backend/login.html', {})
