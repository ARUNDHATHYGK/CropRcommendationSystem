from django.shortcuts import render,redirect    
from Guest.models import *
from Officer.models import *
from User.models import *

def homepage(request):
    return render(request,"Officer/HomePage.html")

def my_pro(request):
    data=tbl_officer.objects.get(id=request.session["oid"])
    return render(request,"Officer/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_officer.objects.get(id=request.session["oid"])
    if request.method=="POST":
        prodata.officer_name=request.POST.get('txtname')
        prodata.officer_contact=request.POST.get('txtcon')
        prodata.officer_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Officer/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Officer/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_officer.objects.filter(id=request.session["oid"],officer_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                officerdata=tbl_officer.objects.get(id=request.session["oid"],officer_password=request.POST.get('txtcurpass'))
                officerdata.officer_password=request.POST.get('txtnewpass')
                officerdata.save()
                return render(request,"Officer/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Officer/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Officer/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Officer/ChangePassword.html")


def notification(request):
    noti=tbl_notification.objects.all()
    if request.method=="POST":
        notiTitle=request.POST.get('txttitle')
        notiDetails=request.POST.get('txtdetails')
        notiDuedate=request.POST.get('txtdate')
        notiPoster=request.FILES.get("fileImage")
        tbl_notification.objects.create(notification_title=notiTitle,notification_details=notiDetails,notification_duedate=notiDuedate,notification_poster=notiPoster)
        return redirect("Officer:notification")
    else:
        return render(request,"Officer/Notification.html",{'data':noti})

def delNotification(request,did):
    tbl_notification.objects.get(id=did).delete()
    return redirect("Officer:notification") 

def applyList(request):
    applydata=tbl_apply.objects.filter(apply_status=0)
    return render(request,"Officer/ApplyList.html",{'applydata':applydata})

def acceptapply(request,aid):
    apply = tbl_apply.objects.get(id=aid)
    apply.apply_status = 1
    apply.save()
    return render(request,"Officer/HomePage.html")

def rejectapply(request,rid):
    apply = tbl_apply.objects.get(id=rid)
    apply.apply_status = 2
    apply.save()
    return render(request,"Officer/HomePage.html")  

def applyListAccepted(request):
    applydata = tbl_apply.objects.filter(apply_status=1)
    return render(request,"Officer/ApplyListAccepted.html",{"applydata":applydata})

def applyListRejected(request):
    applydata = tbl_apply.objects.filter(apply_status=2)
    print(applydata)
    return render(request,"Officer/ApplyListRejected.html",{"applydata":applydata})




        


