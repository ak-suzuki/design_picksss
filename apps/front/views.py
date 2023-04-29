from django.shortcuts import render


def front_top(request):
    print('きました！！')
    return render(request, 'front/index.html', {})
