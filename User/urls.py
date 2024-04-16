from django.urls import path
from User import views
app_name="User"
urlpatterns = [
    
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('ProfessorList/',views.professorList,name="professorList"),
    path('Request/<int:did>',views.request,name="request"),
    path('ViewRequest/',views.viewrequest,name="viewrequest"),
    path('ViewNotification/',views.viewnotification,name="viewnotification"),
    path('Apply/<int:did>',views.apply,name="apply"),
    path('Complaint/',views.complaint,name="complaint"),
    path('ViewApplyList/',views.viewapplyList,name="viewapplyList"),
    path('Feedback/',views.feedback,name="feedback"),

]

