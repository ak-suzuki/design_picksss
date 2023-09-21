from django.contrib import admin
from django.conf.urls import include
from django.urls import path


urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # front user（一般ユーザ向け画面）
    path('', include('frontuser.urls')),
    # administrator（管理者向け画面）
    path('administrator/', include('administrator.urls')),
]
