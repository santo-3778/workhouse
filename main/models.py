from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.



class Moderator(AbstractBaseUser):
    
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    location = models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=250)
    email=models.EmailField()


    # Other fields specific to Moderator model

    def __str__(self):
        return self.username

class User(AbstractBaseUser):
    id=models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    username =models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=128)
    phone_no =models.CharField(max_length=100,unique=True) 
    location =models.CharField(max_length=150)
    user_image =models.ImageField(upload_to="userProfile") 
    dob =models.DateField(null=True)
    user_bio=models.CharField(max_length=150)
    type=models.CharField(max_length=100,default='user') 
    address=models.CharField(max_length=300)

    def __str__(self):
        return self.username

class Worker(AbstractBaseUser):
    
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    username =models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=128)
    phone_no =models.CharField(max_length=100,unique=True)
    location =models.CharField(max_length=150)
    user_image =models.ImageField(upload_to="workerProfile") 
    dob =models.DateField(null=True)
    user_bio=models.CharField(max_length=150)
    type=models.CharField(max_length=100,default='worker') 
    address=models.CharField(max_length=300)
    
    job_title=models.CharField(max_length=150,null= True)
    catagory=models.CharField(max_length=150,null= True)
    experience=models.CharField(max_length=150,null= True)
    skill_1 =models.CharField(max_length=150,null= True)
    skill_2 =models.CharField(max_length=150,null= True)
    skill_3 =models.CharField(max_length=150,null= True)
    id_proof=models.ImageField(upload_to="workerfile")
    exp_proof=models.ImageField(upload_to="workerfile")
    cv=models.ImageField(upload_to="workerfile")

    is_approved=models.BooleanField(null= True)
    status=models.CharField(max_length=100,null= True)
    is_report=models.BooleanField(null= True,default=True)

    def __str__(self):
        return self.username

class login(models.Model):
    username =models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    type=models.CharField(max_length=100)

    def __str__(self):
        return self.username



class Job_post(models.Model):
    post_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title=models.CharField(max_length=150)
    job_description=models.CharField(max_length=350)
    location=models.CharField(max_length=150)
    address=models.CharField(max_length=250)
    time=models.TimeField()
    date=models.DateField()
    min_wage=models.CharField(max_length=150)
    max_wage=models.CharField(max_length=150)
    exp_lvl=models.CharField(max_length=150)
    expected_time=models.CharField(max_length=100)
    valid=models.BooleanField(null=True)
    photo=models.ImageField(upload_to="job_post")


class Notification(models.Model):
    notification_id=models.AutoField(primary_key=True)
    worker=models.ForeignKey(Worker,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Job_post,on_delete=models.CASCADE)


class Message(models.Model):
    message_id=models.AutoField(primary_key=True)
    message=models.CharField(max_length=350)
    sender=models.CharField(max_length=150)
    receiver=models.CharField(max_length=150)

class Report(models.Model):
    report_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    worker=models.ForeignKey(Worker,on_delete=models.CASCADE,null=True)
    reason=models.TextField(blank=False , null= False )
    reported_by=models.CharField(max_length=150)


class Feedback(models.Model):
    feedback_id= models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    worker=models.ForeignKey(Worker,on_delete=models.CASCADE,null=True)
    feedback=models.TextField(blank=False , null= False )   


class job(models.Model):
    job_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    worker=models.ForeignKey(Worker,on_delete=models.CASCADE)
    post_id=models.ForeignKey(Job_post,on_delete=models.CASCADE)
    status=models.CharField(max_length=150,default="pending")