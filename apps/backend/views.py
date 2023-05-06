from django.shortcuts import render, redirect


def sign_in(request):

    return render(request, 'backend/sign_in.html', {})


def sign_out(request):

    # del request.session['staff_id']
    return redirect('sign_in')
