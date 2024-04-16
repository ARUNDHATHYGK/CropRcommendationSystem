from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *


def homepage(request):
    return render(request,"Professor/HomePage.html")

def my_pro(request):
    data=tbl_professor.objects.get(id=request.session["pid"])
    return render(request,"Professor/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_professor.objects.get(id=request.session["pid"])
    if request.method=="POST":
        prodata.professor_name=request.POST.get('txtname')
        prodata.professor_contact=request.POST.get('txtcon')
        prodata.professor_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Professor/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Professor/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_professor.objects.filter(id=request.session["pid"],professor_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                professordata=tbl_professor.objects.get(id=request.session["pid"],professor_password=request.POST.get('txtcurpass'))
                professordata.professor_password=request.POST.get('txtnewpass')
                professordata.save()
                return render(request,"Professor/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Professor/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Professor/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Professor/ChangePassword.html")



def requestList(request):
    requestdata=tbl_request.objects.filter(request_status=0)
    return render(request,"Professor/RequestList.html",{'requestdata':requestdata})

def acceptrequest(request,aid):
    if request.method=="POST":
        arequest = tbl_request.objects.get(id=aid)
        arequest.request_reply=request.POST.get('txtname')
        arequest.request_status = 1
        arequest.save()
        return render(request,"Professor/HomePage.html")
    else:
        return render(request,"Professor/Reply.html")

def rejectrequest(request,rid):
    rrequest = tbl_request.objects.get(id=rid)
    rrequest.request_status = 2
    rrequest.save()
    return render(request,"Professor/HomePage.html")

def requestListAccepted(request):
    requestdata = tbl_request.objects.filter(request_status=1)
    return render(request,"Professor/RequestListAccepted.html",{"requestdata":requestdata})

def requestListRejected(request):
    requestdata = tbl_request.objects.filter(request_status=2)
    print(requestdata)
    return render(request,"Professor/RequestListRejected.html",{"requestdata":requestdata})



