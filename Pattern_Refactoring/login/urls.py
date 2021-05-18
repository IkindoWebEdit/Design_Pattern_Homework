from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.loginPage_GET, name="login"),
    path('login/', views.loginPage_POST, name="login"),
    path('logout/', views.logoutAction, name="logout")
]
