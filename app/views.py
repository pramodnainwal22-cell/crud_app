from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Student
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request,'home.html')

def index(request):
    query = request.GET.get('q')   # search input

    if query:
        data = Student.objects.filter(
            Q(name__icontains=query) | Q(email__icontains=query)
        )
    else:
        data = Student.objects.all()

    return render(request, 'index.html', {'data': data})

def contact(request):
    return render(request,'contact.html')

def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("/login/")

    return render(request,"index.html")

def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']

        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/login/")

    d=Student.objects.get(id=id) 
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=Student.objects.get(id=id) 
    d.delete()
    messages.error(request,"Data deleted Successfully")
    return redirect("/login/")
    
def about(request):
    return render(request,"about.html")

def register(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()

        return redirect('/login')

    return render(request,'register.html')

def user_login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('/login/')

def contact(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        subject = "New Contact Message"

        msg = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """

        send_mail(
            subject,
            msg,
            settings.EMAIL_HOST_USER,
            ['pramodnainwal22@gmail.com']
        )

    return render(request,'contact.html')

