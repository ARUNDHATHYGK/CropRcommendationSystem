from django.shortcuts import render,redirect
from Adminstrator.models import *
from Guest.models import *
from User.models import *

def LodingHomePage(request):
    return render(request,"Adminstrator/HomePage.html")

def ajaxplace(request):
    districtdata=tbl_district.objects.get(id=request.GET.get('disd'))
    placedata=tbl_place.objects.filter(district=districtdata)
    return render(request,"Adminstrator/Ajaxplace.html",{'data':placedata})


def districtInsertSelect(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtname')
        tbl_district.objects.create(district_name=disName)
        return redirect("Adminstrator:districtInsertSelect")
    else:
        return render(request,"Adminstrator/District.html",{'data':dis})

def delDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Adminstrator:districtInsertSelect")

def districtupdate(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        editdata.district_name=request.POST.get("txtname")
        editdata.save()
        return redirect("Adminstrator:districtInsertSelect")
    else:
        return render(request,"Adminstrator\District.html",{"editdata":editdata})    


def AdminregistrationInsertSelect(request):
    adm=tbl_adminregistration.objects.all()
    if request.method=="POST":
        admName=request.POST.get('txtname')
        admContact=request.POST.get('txtcontact')
        admEmail=request.POST.get('txtemail')
        admPassword=request.POST.get('txtpassword')
        tbl_adminregistration.objects.create(Adminregistration_name=admName,Adminregistration_contact=admContact,Adminregistration_email=admEmail,Adminregistration_password=admPassword)
        return redirect("Adminstrator:AdminregistrationInsertSelect")  
    else:
        return render(request,"Adminstrator/Adminregistration.html",{'data':adm})

def delAdminregistration(request,did):
    tbl_adminregistration.objects.get(id=did).delete()
    return redirect("Adminstrator:AdminregistrationInsertSelect")  

def adminregistrationupdate(request,eid):
    editdata=tbl_adminregistration.objects.get(id=eid)
    if request.method=="POST":
        editdata.Adminregistration_name=request.POST.get("txtname")
        editdata.Adminregistration_contact=request.POST.get("txtcontact")
        editdata.Adminregistration_email=request.POST.get("txtemail")
        editdata.Adminregistration_password=request.POST.get("txtpassword")
        editdata.save()
        return redirect("Adminstrator:AdminregistrationInsertSelect")
    else:
        return render(request,"Adminstrator\Adminregistration.html",{"editdata":editdata})          


def Place(request):
    return render(request,"Adminstrator/Place.html")

def placeInsertSelect(request):
    district = tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        placeName=request.POST.get('txtplace')
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=placeName,district=dis)
        return redirect("Adminstrator:placeInsertSelect")
    else:
        return render(request,"Adminstrator/Place.html",{'data':data,"districtdata":district})

def delPlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Adminstrator:placeInsertSelect")

def placeupdate(request,eid):
    district = tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        editdata.place_name=request.POST.get("txtplace")
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.district = dis
        editdata.save()
        return redirect("Adminstrator:placeInsertSelect")
    else:
        return render(request,"Adminstrator\Place.html",{"editdata":editdata,"districtdata":district})


def userListNew(request):
    userdata=tbl_user.objects.filter(user_status=0)
    return render(request,"Adminstrator/UserListNew.html",{'userdata':userdata})

def acceptuser(request,aid):
    user = tbl_user.objects.get(id=aid)
    user.user_status = 1
    user.save()
    return render(request,"Adminstrator/HomePage.html")

def rejectuser(request,rid):
    user = tbl_user.objects.get(id=rid)
    user.user_status = 2
    user.save()
    return render(request,"Adminstrator/HomePage.html")

def userListAccepted(request):
    userdata = tbl_user.objects.filter(user_status=1)
    return render(request,"Adminstrator/UserListAccepted.html",{"userdata":userdata})

def userListRejected(request):
    userdata = tbl_user.objects.filter(user_status=2)
    print(userdata)
    return render(request,"Adminstrator/UserListRejected.html",{"userdata":userdata})




def professorList(request):
    professordata=tbl_professor.objects.filter(professor_status=0)
    return render(request,"Adminstrator/ProfessorList.html",{'professordata':professordata})

def acceptprofessor(request,aid):
    professor = tbl_professor.objects.get(id=aid)
    professor.professor_status = 1
    professor.save()
    return render(request,"Adminstrator/HomePage.html")

def rejectprofessor(request,rid):
    professor = tbl_professor.objects.get(id=rid)
    professor.professor_status = 2
    professor.save()
    return render(request,"Adminstrator/HomePage.html")

def professorListAccepted(request):
    professordata = tbl_professor.objects.filter(professor_status=1)
    return render(request,"Adminstrator/ProfessorListAccepted.html",{"professordata":professordata})

def professorListRejected(request):
    professordata = tbl_professor.objects.filter(professor_status=2)
    print(professordata)
    return render(request,"Adminstrator/ProfessorListRejected.html",{"professordata":professordata})



def officerList(request):
    officerdata=tbl_officer.objects.filter(officer_status=0)
    return render(request,"Adminstrator/OfficerList.html",{'officerdata':officerdata})

def acceptofficer(request,aid):
    officer = tbl_officer.objects.get(id=aid)
    officer.officer_status = 1
    officer.save()
    return render(request,"Adminstrator/HomePage.html")

def rejectofficer(request,rid):
    officer = tbl_officer.objects.get(id=rid)
    officer.officer_status = 2
    officer.save()
    return render(request,"Adminstrator/HomePage.html")

def officerListAccepted(request):
    officerdata = tbl_officer.objects.filter(officer_status=1)
    return render(request,"Adminstrator/OfficerListAccepted.html",{"officerdata":officerdata})

def officerListRejected(request):
    officerdata = tbl_officer.objects.filter(officer_status=2)
    print(officerdata)
    return render(request,"Adminstrator/OfficerListRejected.html",{"officerdata":officerdata})







def complaintList(request):
     data=tbl_complaint.objects.all()
     return render(request,"Adminstrator/ComplaintList.html",{"data":data})


def reply(request,cid):
    data=tbl_complaint.objects.get(id=cid)
    reply=tbl_reply.objects.all()
    if request.method=="POST":
       data.complaint_reply=request.POST.get("txtname")
       data.complaint_staus=1
       data.save()
       return redirect("Adminstrator:reply",cid=cid)
    else:
        return render(request,"Adminstrator/Reply.html",{'data':reply})

def viewfeedback(request):
    data=tbl_feedback.objects.all()
    return render(request,"Adminstrator/ViewFeedback.html",{"data":data})        