from django.urls import path
from Adminstrator import views

app_name="Adminstrator"

urlpatterns = [

    path("HomePage/",views.LodingHomePage,name="LodingHomePage"),


    path("District/", views.districtInsertSelect,name="districtInsertSelect"),
    path("delDistrict/<int:did>", views.delDistrict,name="delDistrict"),
    path("districtupdate/<int:eid>", views.districtupdate,name="districtupdate"),


    path("Adminregistration/", views.AdminregistrationInsertSelect,name="AdminregistrationInsertSelect"),
    path("delAdminregistration/<int:did>", views.delAdminregistration,name="delAdminregistration"),
    path("adminregistrationupdate/<int:eid>", views.adminregistrationupdate,name="adminregistrationupdate"),


    path("Place/", views.placeInsertSelect,name="placeInsertSelect"),
    path("delPlace/<int:did>", views.delPlace,name="delPlace"),
    path("placeupdate/<int:eid>", views.placeupdate,name="placeupdate"),

    path("UserListNew/",views.userListNew,name="userListNew"),
    path("acceptuser/<int:aid>",views.acceptuser,name="acceptuser"),
    path("rejectuser/<int:rid>",views.rejectuser,name="rejectuser"),
    path("UserListAccepted/",views.userListAccepted,name="userListAccepted"),
    path("UserListRejected/",views.userListRejected,name="userListRejected"),
    

    path("ProfessorList/",views.professorList,name="professorList"),
    path("acceptprofessor/<int:aid>",views.acceptprofessor,name="acceptprofessor"),
    path("rejectprofessor/<int:rid>",views.rejectprofessor,name="rejectprofessor"),
    path("ProfessorListAccepted/",views.professorListAccepted,name="professorListAccepted"),
    path("ProfessorListRejected/",views.professorListRejected,name="professorListRejected"),
    

    path("OfficerList/",views.officerList,name="officerList"),
    path("acceptofficer/<int:aid>",views.acceptofficer,name="acceptofficer"),
    path("rejectofficer/<int:rid>",views.rejectofficer,name="rejectofficer"),
    path("OfficerListAccepted/",views.officerListAccepted,name="officerListAccepted"),
    path("OfficerListRejected/",views.officerListRejected,name="officerListRejected"),
    

    path("ComplaintList/", views.complaintList,name="complaintList"),

    path("Reply/<int:cid>",views.reply,name="reply"),

    path('ViewFeedback/',views.viewfeedback,name="viewfeedback"),

    path("logout/",views.logout,name="logout"),

]
