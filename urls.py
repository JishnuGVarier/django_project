from django.urls import path
from.import views

urlpatterns = [
    path(route="login",view=views.loginPageView,name='login'),
    path(route="logincheck",view=views.logincheckView,name='logincheck'),
    path(route="admin",view=views.adminPageView,name='admin'),
    path(route="adddoc",view=views.docPageView,name='adddoc'),
    path(route="savedoc",view=views.savedocView,name='savedoc'),
    path(route="addpat",view=views.patPageView,name='addpat'),
    path(route="savepat",view=views.savepatView,name='savepat'),
]
