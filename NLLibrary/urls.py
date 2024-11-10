"""
URL configuration for NLLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from NLLibrary import settings
import books
import books.views

from django.views.static import serve
from django.urls import re_path

urlpatterns = [

    re_path('static/(?P<path>.*)', serve, {'document_root':settings.STATIC_ROOT}),

    path('admin/', admin.site.urls),

    path('book_add', books.views.book_add),
    path('book_get', books.views.book_get),
    path('book_update', books.views.book_update),
    path('book_delete', books.views.book_delete),
    path('book_delete_forever', books.views.book_delete_forever),
]
