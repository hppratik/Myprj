from django.db import models

# Create your models here.
class User(models.Model):
    userid=models.CharField(max_length=20)
    username=models.CharField(max_length=100)

    class Meta:
        db_table = "user" 

class Client(models.Model):
    clientid= models.CharField(max_length=20)
    clientname= models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)


    class Meta:
        db_table = "client" 

class Project(models.Model):
    projectid= models.CharField(max_length=20)
    projectname= models.CharField(max_length=100)
    clientname= models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    
    class Meta:
        db_table = "project" 


