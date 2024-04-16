from django.shortcuts import render,redirect
from Adminstrator.models import *
from Guest.models import *

# Create your views here.
def ajaxplace(request):
    districtdata=tbl_district.objects.get(id=request.GET.get('disd'))
    placedata=tbl_place.objects.filter(district=districtdata)
    return render(request,"Guest/Ajaxplace.html",{'data':placedata})

def Login(request):
    if request.method == "POST":
        usercount = tbl_user.objects.filter(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password")).count()
        professorcount=tbl_professor.objects.filter(professor_email=request.POST.get("txt_email"),professor_password=request.POST.get("txt_password")).count()
        officercount=tbl_officer.objects.filter(officer_email=request.POST.get("txt_email"),officer_password=request.POST.get("txt_password")).count()
        adminregistrationcount=tbl_adminregistration.objects.filter(Adminregistration_email=request.POST.get("txt_email"),Adminregistration_password=request.POST.get("txt_password")).count()
        if usercount > 0:
            user = tbl_user.objects.get(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"))
            request.session["uid"] = user.id
            request.session["uname"] = user.user_name
            return redirect("User:homepage")
        elif professorcount > 0:
            professor = tbl_professor.objects.get(professor_email=request.POST.get("txt_email"),professor_password=request.POST.get("txt_password"))
            request.session["pid"] = professor.id
            request.session["pname"] = professor.professor_name
            return redirect("Professor:homepage") 
        elif officercount > 0:
            officer = tbl_officer.objects.get(officer_email=request.POST.get("txt_email"),officer_password=request.POST.get("txt_password"))
            request.session["oid"] = officer.id
            request.session["oname"] = officer.officer_name
            return redirect("Officer:homepage")     
        elif adminregistrationcount > 0:
            Adminregistration = tbl_adminregistration.objects.get(Adminregistration_email=request.POST.get("txt_email"),Adminregistration_password=request.POST.get("txt_password"))
            request.session["aid"] = Adminregistration.id
            request.session["aname"] = Adminregistration.Adminregistration_name
            return redirect("Adminstrator:LodingHomePage")         
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"Guest/Login.html")            


def userRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=request.POST.get("txtname"),user_gender=request.POST.get("txtgender"),user_contact=request.POST.get("txtcontact"),user_email=request.POST.get("txtemail"),user_password=request.POST.get("txtpassword"),user_confirmpassword=request.POST.get("txtconfirmpassword"),user_address=request.POST.get("txtaddress"),user_photo=request.FILES.get("fileImage"),place=place)
        return redirect("Guest:userRegistration")
    else:
        return render(request,"Guest/Newuser.html",{"districtdata":district})

def professor(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_professor.objects.create(professor_name=request.POST.get("txtname"),professor_contact=request.POST.get("txtcontact"),professor_email=request.POST.get("txtemail"),professor_password=request.POST.get("txtpassword"),professor_address=request.POST.get("txtaddress"),professor_photo=request.FILES.get("fileImage"),professor_proof=request.FILES.get("fileProof"),place=place)
        return redirect("Guest:professor")
    else:
        return render(request,"Guest/Professor.html",{"districtdata":district})


def officer(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_officer.objects.create(officer_name=request.POST.get("txtname"),officer_contact=request.POST.get("txtcontact"),officer_email=request.POST.get("txtemail"),officer_password=request.POST.get("txtpassword"),officer_address=request.POST.get("txtaddress"),officer_photo=request.FILES.get("fileImage"),officer_proof=request.FILES.get("fileProof"),place=place)
        return redirect("Guest:officer")
    else:
        return render(request,"Guest/Officer.html",{"districtdata":district})  


        
def index(request):
    return render(request,"Guest/index.html")
