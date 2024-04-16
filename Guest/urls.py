from django.urls import path
from Guest import views

app_name="Guest"
urlpatterns = [
    path("Login/", views.Login,name="Login"),
    
    path("Newuser/", views.userRegistration,name="userRegistration"),
    path("Professor/", views.professor,name="professor"),
    path("Officer/", views.officer,name="officer"),
    path("ajaxplace/", views.ajaxplace,name="ajaxplace"),
    path("",views.index,name="index"),

]
