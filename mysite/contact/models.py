from django.db import models
class Contact(models.Model):
    contact_id = models.AutoField
    contact_name = models.CharField(max_length=70)
    contact_email = models.EmailField(max_length=254)
    contact_subject = models.TextField()
    contact_message = models.TextField()
# Create your models here.

class news(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=500,primary_key=True)
    date = models.DateField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class latestNews(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=300)
    userName = models.CharField(max_length=50)
    userProfile = models.CharField(max_length=100)
    views = models.IntegerField()
    likes = models.IntegerField()
    desc = models.CharField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.title
    
class trendingNews(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=500,primary_key=True)
    date = models.DateField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title
    
class subscribe(models.Model):
    mail_id = models.EmailField(primary_key=True)

    def __str__(self):
        return self.mail_id
