from django.urls import path
from Professor import views
app_name="Professor"
urlpatterns = [
    
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path("RequestList/",views.requestList,name="requestList"),
    path("acceptrequest/<int:aid>",views.acceptrequest,name="acceptrequest"),
    path("rejectrequest/<int:rid>",views.rejectrequest,name="rejectrequest"),
    path("RequestListAccepted/",views.requestListAccepted,name="requestListAccepted"),
    path("RequestListRejected/",views.requestListRejected,name="requestListRejected"),

]