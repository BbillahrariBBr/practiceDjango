from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30)
    address = models.TextField()
    
    def __str__(self):
        return f"Name: {self.name}"
    
    #  model inheritance -- 3 types inheritance
    # 1. abstract base class
    # 2. multi-table inheritance
    # 3. proxy model
    
    # abstract base class
    
class CommonInfoClass(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    class  Meta:
        abstract = True
        
class StudentInfoModel(CommonInfoClass): 
    roll = models.IntegerField()
    section = models.CharField(max_length=50)
    payment = models.IntegerField()
    
class TeacherInfoModel(CommonInfoClass):
    salary = models.IntegerField()
    
    
  # 2. multi-table inheritance
class EmployeeModels(models.Model):
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    designation = models.CharField(max_length=30)
    
class ManagerModels(EmployeeModels):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()
    

 # 3. proxy model
 
class Friend(models.Model): #amar frnd class a ache
    school = models.CharField(max_length=40)
    section = models.CharField(max_length=40)
    hw = models.CharField(max_length=40)
    attendence = models.BooleanField()

class Me(Friend): # ami j aj class a nai
    class Meta:
        proxy = True
        ordering = ['id']
    
    
