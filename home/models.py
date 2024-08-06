from django.db import models

# Create your models here.
class Projects(models.Model):
    name=models.CharField(max_length=100,primary_key=True,default=None)
    is_web=models.BooleanField(default=False)
    is_ml=models.BooleanField(default=False)
    desc=models.TextField(default=None,blank=True)
    link=models.URLField(blank=True,default=None) 
    bio=models.CharField(max_length=30,default="Nothing")
    image=models.ImageField(upload_to="home/images/project",default="")
    def __str__(self):
        return self.name
    

class Profile(models.Model):
    name=models.CharField(max_length=30,default=None)
    phone=models.BigIntegerField(default=None,blank=True)
    
    email=models.EmailField(primary_key=True)
    linkedin=models.URLField(default=None,blank=True)
    instagram=models.URLField(default=None,blank=True)
    twitter=models.URLField(default=None,blank=True)
    
    dob=models.DateField(default=None,blank=True)
    address=models.CharField(max_length=50,default=None,blank=True)
    summary=models.TextField(default=None,blank=True)
    bio=models.CharField(max_length=30,default=None)
    image=models.ImageField(upload_to="home/images/profile",blank=True,default="")
    def __str__(self):
        return self.name 


class Team(models.Model):
    project_id=models.ForeignKey(Projects,on_delete=models.CASCADE,default=None)
    member_id=models.ForeignKey(Profile,on_delete=models.CASCADE,default=None)
    class Meta:
        unique_together=('project_id','member_id')
    def __str__(self):
        return self.project_id.name
     



class Education(models.Model):
    id=models.AutoField
    degree=models.CharField(max_length=50)
    start_date=models.IntegerField()
    end_date=models.IntegerField()
    is_cgpa=models.BooleanField()
    marks=models.FloatField()
    school=models.CharField(max_length=50)
    image=models.ImageField(upload_to="home/images/education",default="")
    def __str__(self):
        return self.degree

class Skill(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=30)
    level=models.IntegerField()
    def __str__(self):
        return self.name

class Soft_Skill(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=25)
    level=models.IntegerField()
    def __str__(self):
        return self.name

class Experience(models.Model):
    id=models.AutoField
    title=models.CharField(max_length=30)
    # is_company=models.BooleanField()
    # is_start_date=models.BooleanField()
    company=models.CharField(max_length=30,blank=True,null=True)
    start_date=models.DateField(blank=True,null=True)
    end_date=models.DateField(blank=True,null=True)
    desc=models.TextField()
    image=models.ImageField(upload_to="home/images/experience",default="")
    def __str__(self):
        return self.title



class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.name
    


class Coding_profile(models.Model):
    name=models.CharField(max_length=30)
    link=models.URLField()
    problems=models.IntegerField()
    def __str__(self):
        return self.name

