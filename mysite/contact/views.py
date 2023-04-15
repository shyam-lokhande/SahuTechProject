from django.contrib import messages
from django.shortcuts import render,redirect
from .models import news,latestNews,subscribe
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def home(req):
    total_list = news.objects.order_by('?')[:10]
    object_list1 = news.objects.order_by('?')[:3]
    object_list2 = news.objects.order_by('?')[:4]
    featured_news = news.objects.order_by('?')[:6]
    latest_news1 = latestNews.objects.order_by('?')[:2]
    latest_news2 = latestNews.objects.order_by('?')[:2]
    latest_news3 = news.objects.order_by('?')[:2]
    latest_news4 = news.objects.order_by('?')[:2]
    trending_news1 = news.objects.order_by('?')[:5]
    trending_news2 = news.objects.order_by('?')[:3]
    context = {
        "news1":object_list1,
        "news2":object_list2,
        "featured_news":featured_news,
        "latest_news1":latest_news1,
        "latest_news2":latest_news2,
        "latest_news3":latest_news3,
        "latest_news4":latest_news4,
        "trending_news1":trending_news1,
        "trending_news2":trending_news2,

    }

    
    return render(req,"index.html",context)

def single(req):
    return render(req,"single.html")

def contact(req):
    return render(req,"contact.html")

def category(req):
    return render(req,"category.html")

def subscribe(req):
    if req.method=='POST':
        email = req.POST.get('email')
        if not email:
            messages.error(req,'Please enter the email')
            return redirect('/')
        
        if subscribe.objects.filter(mail_id=email):
            messages.error(req,'This email is already registerd')
            return redirect('/')
        
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(req,e.messages[0])

        subscrib_instance = subscribe(mail_id=email)
        subscrib_instance.save()
        redirect(req.META.get('HTTP_REFERER','/'))

