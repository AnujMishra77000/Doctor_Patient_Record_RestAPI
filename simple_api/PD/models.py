from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    Department=models.CharField(max_length=50)
    Diagnostics = models.CharField(max_length=250)
    Location= models.CharField(max_length=100)
    Specialization = models.CharField(max_length=200) 
    
    def __str__(self):
        return self.Department
    
class Doctors(models.Model):
    Name=models.CharField(max_length=100)
    department= models.ForeignKey(Department, on_delete=models.CASCADE, related_name="Doctors" )
    Specialization=models.CharField(max_length=100)
  
    def __str__(self):
        return self.Name
    
class Petient_Record(models.Model):
    PetitentID = models.IntegerField()
    name= models.CharField(max_length=100, default="Petient")
    age=models.IntegerField(default=18)
    DepartmentId = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="Petient_Record")
    DoctorID=models.ForeignKey(Doctors, on_delete=models.CASCADE)
    Created_date = models.DateField(auto_now_add=True)
    Diagnostics = models.CharField(max_length=50,)
    Observations = models.CharField(max_length=255)
    misc = models.CharField(max_length=255, blank= True)

    def __str__(self):
        return self.name

     

