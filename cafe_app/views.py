from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout




# Create your views here.
def about(request):
    return HttpResponse("<h1>This is about page</h1>")

def contact(request):
    return HttpResponse("<h1>This is contact page</h1>")

def edit(request,rid):
    print("id to be edited : ", rid)
    return HttpResponse("id to be edited : "+rid)

def addition(request,x1,x2):
    s=int(x1)+int(x2)
    s1=str(s)
    return HttpResponse("Addition is : "+s1)

class SimpleView(View):
    def get(self,request):
        return HttpResponse("Hello from simple view")

def hello(request):
    context={}
    context['greet']="good eving, we are learning DTL"
    context['x']=100
    context['y']=200
    context['l']=10,20,30,40,50,60
    context['products']=[
        {'id':1,'name':'hot coffee','cat':'coffee','price':70},
        {'id':2,'name':'dessert','cat':'dessert','price':100},
            
            ]
    return render(request, 'hello.html', context) 

def home(request):
    return render(request,'home.html')

def menu(request):
    return render(request,'menu.html')

def gallery(request):
    return render(request,'gallery.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        context={}
        if uname=="" or upass=="" or ucpass=="":
            context['errmsg']="fields can not be empty"
            return render(request,'register.html', context)
        elif upass!=ucpass:
            context['errmsg']="password and confirm passsword didn`t match"
            return render(request,'register.html', context)
        else:
            try:
                u=User.objects.create(password=upass,username=uname,email=uname)
                u.set_password(upass)
                u.save()
                context['success']="User created successfully, Please Login"
                return render(request,'register.html',context)
                #return HttpResponse("User created successfully")
            except Exception:
                context['errmsg']="user with same name already Exist"
                return render(request,'register.html',context)
    else:
        return render(request, 'register.html')


def user_login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        context={}
        if uname=="" or upass=="":
            context['errmsg']="fields can not be empty"
            return render(request,'login.html', context)
        else:
            u=authenticate(username=uname, password=upass)
            #print(u) #object
            if u is not None:
                login(request, u)   #start session
                return redirect('/home')
            else:
                context['errmsg']="Invalid Username and password"
                return render(request,'login.html', context)
            # print(uname,"--",upass)
            #return HttpResponse("Data is Fetched")
    else:
        return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('/home')

def book_table(request):
    if request.method=='POST':
        cname=request.POST['cname']
        cemail=request.POST['cemail']
        cphone=request.POST['cphone']
        cdate=request.POST['cdate'] 
        ctime=request.POST['ctime'] 
        cpeople=request.POST['cpeople']
       # c=User.objects.create(name=cname,email=cemail,phone=cphone,date=cdate,time=ctime,people=cpeople)
        #c.save()
        return HttpResponse("date inserted")
        pass
    else:
        return render(request, 'book_table.html')