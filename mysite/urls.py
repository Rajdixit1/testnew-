"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from mysite import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aboutus/',view.aboutus),
    path('',view.homepage),
    path('save/',view.save),
    path('calculator/',view.calculator),
    path('newhome/',view.homePage),
    path('courseDetails/<int:courseid>',view.courseDetails),
    path('courseDetails/<str:courseid>',view.courseDetails),
    path('courseDetails/<slug:courseid>',view.courseDetails),

]
