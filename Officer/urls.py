from django.urls import path
from Officer import views
app_name="Officer"
urlpatterns = [
    
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('Notification/',views.notification,name="notification"),
    path("delNotification/<int:did>", views.delNotification,name="delNotification"),
    
    path("ApplyList/",views.applyList,name="applyList"),
    path("acceptapply/<int:aid>",views.acceptapply,name="acceptapply"),
    path("rejectapply/<int:rid>",views.rejectapply,name="rejectapply"),
    path("ApplyListAccepted/",views.applyListAccepted,name="applyListAccepted"),
    path("ApplyListRejected/",views.applyListRejected,name="applyListRejected"),

    


]