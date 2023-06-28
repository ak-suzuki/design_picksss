from django.shortcuts import render, redirect


def sign_in(request):

    return render(request, 'administrator/sign_in.html', {})


def sign_out(request):

    return redirect('sign_in')
