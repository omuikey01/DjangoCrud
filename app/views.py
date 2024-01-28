from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import RegisterForm, LoginForm
from .models import RegisterModel, QueryModel
from datetime import datetime
from django.db.models import Q
# Create your views here.


# regisForm = RegisterForm()
registrationform= {}
registrationform['Rform'] = RegisterForm()
loginform ={}
loginform['Lform'] = LoginForm()

def homepage(request):
    return render(request, "app/index.html")

def registerpage(request):
    return render(request, "app/registration.html", {"form" : registrationform})

def logoutpage(request):
    print("***********************")
    return render(request, "app/index.html")


def loginpage(request):
    return render(request, "app/login.html", {"form" : loginform})



def registerpageData(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            pass1 = request.POST['password']
            pass2 = request.POST['confirm_pass']

            user = RegisterModel.objects.filter(email = email)
            if user:
                msg = "Email is Already Exixst"
                return render(request, "app/registration.html", {"form" : registrationform, "msg" : msg })
            else :
                RegisterModel.objects.create(
                    name = name,
                    email = email,
                    contact = contact,
                    password = pass1,
                    confirm_pass = pass2
                )
                return render(request, "app/login.html", {"form" : loginform})
        else :
            return render(request, "app/registration.html", {"form" : registrationform, "msg" : "Information Required"})
    except:
        return render(request, "app/registration.html", {"form" : registrationform, "msg" : "Information Required"})


def loginDataData(request):
    try:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = RegisterModel.objects.filter(email = email)

            if user[0].email == email and user[0].password == password:
                userdetails = {
                    "name" : user[0].name,
                    "email" : user[0].email,
                }
                return render(request, "app/deshboard.html", {"data" : userdetails})
            else :
                msg = "username and password not match !!"
                return render(request, "app/login.html", {"msg" : msg, "form" : loginform})
        else :
            return render(request, "app/login.html", {"msg" : "Userid and Password Required!!", "form" : loginform})
    except:
        return render(request, "app/login.html", {"msg" : "Userid and Password Required!!", "form" : loginform})



def queryDatapage(request):
    if request.method == "POST":
        uname = request.POST['name']
        uemail = request.POST['email']
        uquery = request.POST['query']
        udate = datetime.today()
        user = RegisterModel.objects.filter(email = uemail)
        userdetails = {
            "name" : user[0].name,
            "email" : user[0].email,
        }
        QueryModel.objects.create(
            name = uname,
            query = uquery,
            date = udate,
            email = uemail
        )
        return render(request, "app/deshboard.html", {"data" : userdetails})
    else :
        return render(request, "app/deshboard.html", {"data" : "Data Need Post not a Get "})
    


def showqueryDatapage(request):
    if request.method == 'POST':
        email = request.POST['SQBtn']
        QueryData = QueryModel.objects.filter(email = email)
        user = RegisterModel.objects.filter(email = email)
        userdetails = {
            "name" : user[0].name,
            "email" : user[0].email,
            }
        if QueryData :
            return render(request, "app/deshboard.html", {"data" : userdetails, "querydata" : QueryData})
        else :
            return render(request, "app/deshboard.html", {"data" : userdetails, "NoQuery" : "No Query Yet "})

    

def Deletepage(request, mail, idd):
    user = RegisterModel.objects.filter(email = mail)
    userdetails = {
            "name" : user[0].name,
            "email" : user[0].email,
        }
    data = QueryModel.objects.filter(id = idd).delete()
    QueryData = QueryModel.objects.filter(email = mail)
    return render(request, "app/deshboard.html", {"data" : userdetails, "querydata" : QueryData})


def editpage(request, mail, idd):
    querydata = QueryModel.objects.filter( Q(email = mail) & Q(id=idd) )
    user = RegisterModel.objects.filter(email = mail)
    query = querydata[0].query
    userdetails = {
            "name" : user[0].name,
            "email" : user[0].email,
            "query" : query,
            "idd" : idd
        }
    return render(request, "app/deshboard.html", { "data" : userdetails, "update" : userdetails})




def updatequerydatapage(request, idd):
    if request.method == 'POST':
        uname = request.POST['name']
        uemail = request.POST['email']
        uquery = request.POST['query']
        # udate = datetime.today()
        
        user = RegisterModel.objects.filter(email = uemail)
        userdetails = {
                "name" : user[0].name,
                "email" : user[0].email,
            }
        user = QueryModel.objects.filter(id=idd)
        # print("**************")
                
        # QueryModel.objects.create(query = uquery )
        return render(request, "app/deshboard.html", {"data" : userdetails})
    
def search(request, mail):
    if request.method == 'POST':
        search = request.POST['search']
        user = RegisterModel.objects.filter(email = mail)
        userdetails = {
                "name" : user[0].name,
                "email" : user[0].email,
            }
        querydata = QueryModel.objects.filter( Q(email = mail) & Q( query=search) )
        if querydata :
            return render(request, "app/deshboard.html", {"data" : userdetails, "querydata" : querydata })
        else :
            return render(request, "app/deshboard.html", {"data" : userdetails, "querydata" : querydata, "NoQuery" : "No Found Search Data !!" })
            