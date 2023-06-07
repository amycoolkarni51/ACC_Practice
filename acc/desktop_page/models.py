from django.db import models

# Create your models here.
class Contact(models.Model):
    Full_Name = models.CharField(max_length=20)
    EmailId = models.EmailField()
    Subject = models.CharField(max_length=100)
    Message = models.CharField(max_length=255)
    
    class Meta:
        db_table="contact"
        

"""class Register(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    UserName = models.CharField(max_length=10)
    Address = models.TextField()
    Profession = models.CharField(max_length=20)
    Courses = models.CharField(max_length=20)
    EmailId = models.EmailField()
    Password = models.CharField(max_length=8)
    
    class Meta:
        db_table="register"
    
class Login(models.Model):
    UserName = models.CharField(max_length=10)
    EmailId = models.EmailField()
    Password = models.CharField(max_length=8)
    
    class Meta:
        db_table="login"   """
    
