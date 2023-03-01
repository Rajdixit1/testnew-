from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")

def save(request):
    add = 0
    try:
        n1=int(request.GET['num1'])
        n2=int(request.GET['num2'])
        add=n1+n2
    except:
        pass
    return render(request,"form.html",{'output':add})

def aboutus(request):
    return HttpResponse("wlcome sunil")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def homepage(request):
     data={
        'title':'Home Page',
        'bdata':'welcome bro',
        'namelist':['hello','sunil','kumar'],
        'number':[10,20,30,40,50],
        'student_details':[{'name':'sunil','phone': 9905105846},{'name':'kumar','phone':8987614649}]
    }
     return render(request,"index.html",data)

def calculator(request):
    c = 0
    try:
        n1=eval(request.GET['num1'])
        n2=eval(request.GET['num2'])
        opr =request.GET['operation']
        if opr =="+":
            c=n1+n2
        elif opr =="-":
            c=n1-n2
        elif opr =="*":
            c=n1*n2
        elif opr =="/":
            c=n1/n2
    except:
        pass
    return render(request,"calculator.html",{'output':c})
    
