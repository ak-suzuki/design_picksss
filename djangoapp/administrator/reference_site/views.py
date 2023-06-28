from django.shortcuts import render


def item_list(request):
    """ 参考サイト一覧"""
    context = {}
    return render(
        request,
        'administrator/reference_site/item_list.html',
        context
        )


def item_add(request):
    """ 参考サイト追加"""
    context = {}
    return render(
        request,
        'administrator/reference_site/item_add.html',
        context
        )