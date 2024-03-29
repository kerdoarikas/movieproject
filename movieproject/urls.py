"""
URL configuration for movieproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("movieapp/", include("movieapp.urls")), # rida ütleb et movieapp lingid on failis "movieapp.urls"
    path("", RedirectView.as_view(url="movieapp")) # kui on http://127.0.0.1:8000 siis see rida
                                                    # lisab "movieapp" ehk http://127.0.0.1:8000/movieapp/
                                        # kui vaatad api urls.py, seal on avaleht "", mis tähendab et kui on
                                # http://127.0.0.1:8000/movieapp/"siin on tühi", siis teab et vaja avada avaleht

]
