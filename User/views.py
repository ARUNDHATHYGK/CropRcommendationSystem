from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Officer.models import *

def homepage(request):
    return render(request,"User/HomePage.html")

def my_pro(request):
    data=tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        prodata.user_name=request.POST.get('txtname')
        prodata.user_contact=request.POST.get('txtcon')
        prodata.user_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"User/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"User/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_user.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_user.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcurpass'))
                userdata.user_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"User/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"User/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"User/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"User/ChangePassword.html")


def professorList(request):
    data=tbl_professor.objects.all()
    return render(request,"User/ProfessorList.html",{'data':data})


def request(request,did):
    req=tbl_request.objects.all()
    profess=tbl_professor.objects.get(id=did)
    userdata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        reqTitle=request.POST.get('txttitle')
        reqDetails=request.POST.get('txtdetails')
        tbl_request.objects.create(request_title=reqTitle,request_details=reqDetails,user=userdata,professor=profess)
        return redirect("User:professorList")
    else:
        return render(request,"User/Request.html",{'data':req})

def viewrequest(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    data=tbl_request.objects.filter(user=prodata)
    return render(request,"User/ViewRequest.html",{'data':data})

def viewnotification(request):
    data=tbl_notification.objects.all()
    return render(request,"User/ViewNotification.html",{'data':data})



def apply(request,did):
    userdata=tbl_user.objects.get(id=request.session["uid"])
    did=tbl_notification.objects.get(id=did)
    tbl_apply.objects.create(user=userdata,notification=did)
    return redirect("User:homepage")


def complaint(request):
    complaint = tbl_complaint.objects.all()
    userdata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        complainttitle=request.POST.get('txttitle')
        complaintdetails=request.POST.get('txtdetails')
        tbl_complaint.objects.create(complaint_title=complainttitle,complaint_details=complaintdetails,user=userdata)
        return redirect("User:complaint")
    else:
        return render(request,"User/Complaint.html",{"data":complaint})

def viewapplyList(request):
    data=tbl_apply.objects.all()
    return render(request,"User/ViewApplyList.html",{'data':data})   

def feedback(request):
    feedback = tbl_feedback.objects.all()
    if request.method=="POST":
        feedbacktitle=request.POST.get('txttitle')
        feedbackdetails=request.POST.get('txtdetails')
        tbl_feedback.objects.create(feedback_title=feedbacktitle,feedback_details=feedbackdetails)
        return redirect("User:feedback")
    else:
        return render(request,"User/Feedback.html",{"data":feedback})         


        




