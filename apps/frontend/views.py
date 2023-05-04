from django.shortcuts import render


def index(request):
    print('きました！！')
    return render(request, 'frontend/index.html', {})
