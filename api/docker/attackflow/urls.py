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
    # Pages
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login/', views.login),
    path('users/<int>/', views.users),
    path('annotate/<int:report_id>/', views.annotate_redirect),
    path('annotate/<int:report_id>/view/', views.annotation_view_page),
    path('annotate/<int:report_id>/edit/', views.annotation_edit_page),
    # Requests
    path('json/users/login/', views.login),
    path('json/users/signup/', views.signup),
    path('json/current_reports/create', views.upload_report)
]

"""
    endpoints: 
        - create user
            - recieve: username, password
        - login //not sure how to check this with hashed password
            - recieve: username, password
        - edit user
            - recieve: username, password
            - resposnse(?): username
        - get all the documents for the user (if admin get all the documents)
            - recieve: user id
            - response: all documents created by user id
        - upload document
            - recieve: document details
        - return document with annotations
            - recieve: document id
            - response: document details
        - update the annotations (bases on document id)
            - recieve: annotations, document id
        - call document based on ID
            - recieve: document id
            - response: document details
"""