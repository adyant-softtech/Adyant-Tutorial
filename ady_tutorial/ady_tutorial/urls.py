"""ady_tutorial URL Configuration

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
from django.urls import path, include
from tutorial_api import views as api_views
from tutorial import views
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from tutorial_api.api import auth

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'students', api_views.StudentViewSet)
# router.register(r'students-details', api_views.GetStudentsById.as_view(), name='students')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('home/', views.home),
    path('welcome/', views.welcome),
    path('adyant/', views.adyant),
    path('register/', views.registerform),
    path('update/', views.updateForm),
    path('students/', views.StudentListView.as_view(), name='students'),
    path('students-detail/', views.StudentData.as_view()),
    path('students/create', views.StudentCreateView.as_view()),
    #path('<pk>/', views.StudentDetailView.as_view()),
    #path(r'students/<id>', api_views.GetStudentsById.as_view(), name='students'),
    path(r'students/<id>', api_views.GetStudentsByIds, name='students'),
    path(r'tutorial/v1/api/auth', api_views.get_auth_key),
    path(r'tutorial/v1/api/auth-token', auth_views.obtain_auth_token),
    path(r'tutorial/v1/api/get-auth-token', auth.CustomAuthToken.as_view()),

    path('api/', include(router.urls)),

    path('api-auth/', include('rest_framework.urls'))
]