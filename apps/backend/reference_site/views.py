from django.shortcuts import render


def reference_site_list(request):
    return render(request, 'backend/reference_site_list.html', {})
