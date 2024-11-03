from django.db import models

# Create your models here.
class student(models.Model):
    id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    rollno=models.IntegerField()
    city=models.CharField(max_length=150)
    
    def __str__(self):
        return self.name