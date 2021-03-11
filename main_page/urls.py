"""main_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from search_bypass import views as search_views
from mp4_mp3 import views as converter_views


urlpatterns = [
    path('', include('main_page_app.urls')),
    path('search_bypass/',search_views.search_page, name = 'search'),
    path('search/', search_views.search_fun, name = 'search_bypass'),

    path('convert/',converter_views.home_convert_page, name = 'convert_home'),
    path('admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()