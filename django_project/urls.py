"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from appdearte import views

urlpatterns = [
  path('', views.homepage, name="home"),
  path('admin/', admin.site.urls),
  path('search/', views.searchpage, name = 'search'),
  path('users', views.create_user),
  path('users/login/', views.login_user, name="login"),
  path('users/logout/', views.logout_user, name="logout"),
  path('avaliation_form/<str:pk>/', views.avaliation_form, name="avaliation_form"), 
  path('more-about-us/', views.know_more)
]
