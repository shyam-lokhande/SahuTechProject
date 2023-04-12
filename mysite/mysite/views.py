from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import Userinfo
from contact.models import Contact

def homepage(request):
    # data = {
    #     'title': 'Home New',
    #     'bdata': 'Welcome to mysite',
    #     'clist': ['PHP','Java','Django'],
    #     'numbers':[10,20,30,40,50],
    #     'student_details' :[
    #         {'name': 'pradeep','phone': 5432116789},
    #         {'name': 'jaideep','phone': 5432116689}
    #     ]
    # }
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        en = Contact(contact_name=name,contact_email=email,contact_subject=subject,contact_message=message)
        en.save()
    return render(request,"contact.html")

def category(request):
    return render(request,"category.html")

def single(request):
    return render(request,"single.html")

def Form(request):
    fn=Userinfo()
    # data is dictionary name
    data={'form':fn}

    try:
        if request.method=="POST":
            v1=request.POST.get('n1')
            v2=request.POST.get('n2')
            v3=request.POST.get('n3')
            v4=request.POST.get('n4')
            #data={'form':fn}
            #url="/category/"
            
            
            return HttpResponseRedirect('/category/')
    except:
        pass
    return render(request,"contact.html")