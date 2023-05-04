from django.contrib import admin
from django.conf.urls import include
from django.urls import path


urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # frontend（一般ユーザ向け画面）
    path('', include('apps.frontend.urls')),
    # backend（管理者向け画面）
    path('administrator/', include('apps.backend.urls')),
]
