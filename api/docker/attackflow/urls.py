"""
URL configuration for attackflow project.

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
from django.urls import path
from . import views

# all urls should have a trailing slash /
# by specifying http_method_names you can limit what requests are accepted by a url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('login/', views.login_page),
    path('user/<int>/', views.user_page),
    path('json/user/login/', views.login),
    path('json/user/signup/', views.signup),
    path('annotate/<int:report_id>/', views.annotate_redirect),
    path('annotate/<int:report_id>/view/', views.annotation_view_page),
    path('annotate/<int:report_id>/edit/', views.annotation_edit_page),
    path('upload_report/', views.upload_report)
]