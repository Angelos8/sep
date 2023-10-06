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
    path('', views.home_view, name='home_page'),
    path('deleteAll/', views.delete_all_users),
    path('displayUser/', views.display_all_users),
    path('login/', views.login, name='login_page'),
    path('signup/', views.signup),
    path('deleteAll/', views.delete_all_users),
    path('logout/', views.logout),
    path('displayUser/', views.display_all_users),
    # path('login/', views.login_view, name='login_page'),
    # path('login/verify/', views.verify_login,name='verify_login'),
    # path('logout/', views.logout),
    # path('signup/', views.signup_view),
    # path('signup/verify/', views.verify_signup,name='verify_signup'),
    path('users/', views.login_redirect), # redirect user to login page in not logged in
    path('users/<int:user_id>', views.users_view),
    path('users/<int:user_id>/settings', views.settings_view),
    path('users/<int:user_id>/update', views.update_user),
    path('users/<int:user_id>/delete', views.delete_user),
    path('users/<int:user_id>/upload_report', views.upload_report),
    path('annotate/<int:report_id>/edit', views.edit_annotations_view),
    path('annotate/<int:report_id>/inspect', views.inspect_annotations_view),
    path('annotate/new', views.annotate_new_report_view)
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