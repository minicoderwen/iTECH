<<<<<<<< HEAD:tango_with_django_project/tango_with_django_project/urls.py
"""tango_with_django_project URL Configuration
========
"""iTECH URL Configuration
>>>>>>>> a7c67f6 (initial commit):iTECH/urls.py

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blog import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('blog/', include('blog.urls')),
    path('authentication/', include('authentication.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 这样就可以直接在浏览器中访问media中的资源了，默认是static，所以static中的资源也可以直接访问。


