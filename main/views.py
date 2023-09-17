from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages 
from django.contrib import auth 
from django.contrib.auth import authenticate , login ,logout
from django.db.models import Q


from main.models import Moderator, User, Worker ,Job_post,Notification,Message,Report,Feedback



# Create your views here.
def my_view(request):

    return render(request,"index.html")



def user_home(request):
    username = request.session.get('username')
    users =User.objects.all()
    for i in users:
        if i.username == username:
            f_name=i.first_name
            l_name=i.last_name
            img=i.user_image


    user= User.objects.get(username=username )
    job_posts = Job_post.objects.filter(user_id=user)
    worker = Worker.objects.all()
    notifications=Notification.objects.filter(user = user)
    msg=Message.objects.filter(receiver = user.username)
    

    context = {'username':username,'f_name':f_name,'l_name':l_name,'img':img, 'history':job_posts, 'worker':worker, 'notifications':notifications,'msg':msg}                            

    return render(request,"userhome.html",context)

def worker_home(request):
    
    username = request.session.get('username')
    worker=Worker.objects.get(username = username)
    msg=Message.objects.filter(receiver = worker.username)
    if worker.status == 'Active' and worker.is_approved == True and worker.is_report == False: 
        post=Job_post.objects.filter(Q(job_title=worker.job_title) & Q(location=worker.location))
        context = {'worker':worker, 'post':post, 'message':msg}
    else:
        context = {'worker':worker ,'message':msg,}
    return render(request,"workhome.html",context)


def my_radio_view(request):
    
    status = request.GET.get('selected_value', None)
    print(status)
    username = request.session.get('username')
    worker=Worker.objects.get(username = username)
    worker.status=status
    worker.save()
    return redirect('/worker_home')

def moderator_home(request):
    username = request.session.get('username')
    mod=Moderator.objects.get(username = username)
    worker=Worker.objects.all()
    post=Job_post.objects.all()
    user=User.objects.all()
    feed=Feedback.objects.all()
    context={'mod':mod,'worker':worker,'user':user,'post':post,'feed':feed}


    return render(request,"moderatorhome.html",context)



def admin_home(request):
    if request.method != "POST":
        return _extracted_from_admin_home_3(request)
    username = request.POST.get('username')
    password = request.POST.get('password')
    address = request.POST.get('address')
    phone = request.POST.get('phoneno')
    email=request.POST.get('email')
    location=request.POST.get('location')


    moderator=Moderator.objects.filter(username = username)
    if moderator.exists():
        messages.info(request,'username already exists ')
        return redirect('/admin_home')

    moderator = Moderator.objects.create(

       username = username,
       address =address,      
       phone = phone,       
       location = location,
       email = email,      

    )
    moderator.set_password(password)
    moderator.save()
    messages.info(request,'registered sucessfully')
    return redirect('/admin_home')


# TODO Rename this here and in `admin_home`
def _extracted_from_admin_home_3(request):
    user=User.objects.all()
    worker=Worker.objects.all()
    mod=Moderator.objects.all()
    post=Job_post.objects.all()
    context ={'user':user,'worker':worker,'mod':mod,'post':post}
    return render(request,'admin_home.html',context)

def admin_worker(request):
    user=User.objects.all()
    worker=Worker.objects.all()
    mod=Moderator.objects.all()
    post=Job_post.objects.all()
    context ={'user':user,'worker':worker,'mod':mod,'post':post}
    return render(request,"admin_worker.html",context)

def moderator_delete(request,id):
    queryset = Moderator.objects.get(id = id)
    queryset.delete()
    return redirect('/admin_home')

def worker_delete(request,id):
    queryset = Worker.objects.get(id = id)
    queryset.delete()
    return redirect('/admin_worker')

def job_post(request):
    username = request.session.get('username')
    users =User.objects.all()
    for i in users:
        if i.username == username:
            f_name=i.first_name
            l_name=i.last_name
            img=i.user_image
    context = {'username':username,'f_name':f_name,'l_name':l_name,'img':img}

    if request.method == "POST":
        job_title=request.POST.get('job_title')
        job_description=request.POST.get('job_description')
        location=request.POST.get('location')
        address=request.POST.get('address')
        time=request.POST.get('time')
        date=request.POST.get('date')
        min_wage=request.POST.get('min_wage')
        max_wage=request.POST.get('max_wage')
        exp_lvl=request.POST.get('exp_lvl')
        expected_time=request.POST.get('expected_time')
        photo=request.FILES.get('photo')

        user_id = request.session.get('id')

        Job_post.objects.create(
        job_title=job_title, 
        job_description=job_description,
        location=location,
        address=address,
        time=time,
        date=date,
        min_wage=min_wage,
        max_wage=max_wage,
        exp_lvl=exp_lvl,
        expected_time=expected_time,
        photo=photo,
        user_id=user_id           

        )
        messages.info(request,'created sucessfully')
        
    return render(request,"jobpost.html",context)


def post_delete(request,id):
    queryset = Job_post.objects.get(post_id = id)
    queryset.delete()
    return redirect('/user_home')


def status(request,post):
    post=Job_post.objects.filter(job_title = Worker.job_title)
    
    return (post)     
    

#how to accept a value from radio button in html page in views.py?


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'admin':
            print("Login successful")
            return redirect('/admin_home')

        user = auth.authenticate(request, username = username,password = password)

        print (user)
        if user is None:
            messages.error(request , 'invalid username or password')
            return redirect('/login_view')
        else:
            if isinstance(user, Moderator):
                login(request, user)
                return _extracted_from_login_view_21(request, user, 'moderator_home')
            elif isinstance(user, User):
                return _extracted_from_login_view_21(request, user, 'user_home')
            elif isinstance(user, Worker):
                return _extracted_from_login_view_21(request, user, 'worker_home')
    return render(request,"login.html")


# TODO Rename this here and in `login_view`
def _extracted_from_login_view_21(request, user, arg2):
    login(request, user)
    request.session['username'] = request.user.username
    request.session['id'] = request.user.id
    return redirect(arg2)

  

def logout_view(request):
    logout(request)
    return redirect('/login_view')




def user_reg(request):
    if request.method != "POST":
        return render(request,'userreg.html')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    dob =request.POST.get('dob')
    address = request.POST.get('address')
    phoneno = request.POST.get('phoneno')
    user_bio =request.POST.get('user_bio')  
    email=request.POST.get('email')
    user_image=request.FILES.get('user_image')
    location=request.POST.get('location')
    _type=request.POST.get('type')

    user=User.objects.filter(username = username)
    if user.exists():
        messages.info(request,'username already exists ')
        return redirect('/user_reg')

    user = User.objects.create(
       first_name = first_name,
       last_name = last_name,
       username = username,
       address =address,
       dob =dob,
       phone_no = phoneno,
       user_bio = user_bio,
       location = location,
       email = email,
       user_image = user_image,
       type = _type

    )
    user.set_password(password)
    user.save()
    messages.info(request,'registered sucessfully')
    return redirect('/user_reg')

    


def worker_reg(request):
    if request.method != "POST":
       return render(request,'workerreg.html')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    dob =request.POST.get('dob')
    address = request.POST.get('address')
    phoneno = request.POST.get('phoneno')
    user_bio =request.POST.get('user_bio')  
    email=request.POST.get('email')
    user_image=request.FILES.get('user_image')
    location=request.POST.get('location')
    _type=request.POST.get('type')

    
    worker=Worker.objects.filter(username = username)
    if worker.exists():
        messages.info(request,'username already exists ')
        return redirect('/worker_reg')
    
    worker = Worker.objects.create(
       first_name = first_name,
       last_name = last_name,
       username = username,
       address =address,
       dob =dob,
       phone_no = phoneno,
       user_bio = user_bio,
       location = location,
       email = email,
       user_image = user_image,
       type = _type

    )
    worker.set_password(password)
    worker.save()
    messages.info(request,'registered sucessfully')
    return redirect('/worker_reg')

def worker_valid(request):
    username = request.session.get('username')
    worker=Worker.objects.get(username = username)
    if request.method == "POST":
        worker.job_title = request.POST.get('job_title')
        worker.catagory = request.POST.get('catagory')
        worker.experience = request.POST.get('experience')
        worker.skill_1 = request.POST.get('skill_1')
        worker.skill_2 = request.POST.get('skill_2')
        worker.skill_3 = request.POST.get('skill_3')
        worker.id_proof = request.FILES.get('id_proof')
        worker.exp_proof = request.FILES.get('exp_proof')
        worker.cv = request.FILES.get('cv')
        worker.save()
        messages.info(request,'submitted sucessfully')   
    context ={'worker':worker}
    return render(request,"workervalidation.html",context)

   


def contact_view(request):

    return render(request,"contact.html")


def about_view(request):

    return render(request,"about.html")

def job_single(request,id):
   username = request.session.get('username')
   worker=Worker.objects.get(username = username)
   post=Job_post.objects.get(post_id = id)
   context = {'worker':worker , 'post':post}

   return render(request,"job_single.html",context)


def notify(request,id):
   username = request.session.get('username')
   worker=Worker.objects.get(username = username)
   post=Job_post.objects.get(post_id = id)
   

   notification = Notification.objects.create(
       worker=worker,
       user=post.user,
       post=post
   )
   notification.save()
   
   print(notification)
   return redirect('/worker_home')


def get_notifications(request,id):
   notifications=Notification.objects.get(notification_id = id)
   notifications.delete()
   context={'list':notifications}
   return render(request,"chat.html",context) 
   
   



from django.http import JsonResponse
from .models import Message

def send_message(request):
   if request.method == 'POST':
        import json

        data = json.loads(request.body)
        msg = data.get('msg')
        sender = data.get('sender')
        receiver = data.get('receiver')

        message=Message.objects.create(
            sender=sender,
            receiver=receiver,
            message=msg
            )
        message.save()
        return JsonResponse({'status': 'success'})
   
   return JsonResponse({'status': 'error'})

def send_feedback(request):
   if request.method == 'POST':
        import json

        data = json.loads(request.body)
        feedback = data.get('feedback')
        
        worker = data.get('worker')
        worker =Worker.objects.get(username = worker)

        feedback=Feedback.objects.create(
            
            worker=worker,
            feedback=feedback
            )
        feedback.save()
        return JsonResponse({'status': 'success'})
   
   return JsonResponse({'status': 'error'})



def get_messages(request,sender):
    username = request.session.get('username')
    worker= Worker.objects.get(username=username )
    msg=Message.objects.filter(sender = sender)
    context={'msg':msg,'worker':worker,'sender':sender}
    
    return render(request,"message_worker.html",context)
   
def get_user_messages(request,sender):
    username = request.session.get('username')
    user=User.objects.get(username = username)
    msg = Message.objects.filter(Q(sender=sender) & Q(receiver=user))
    context={'msg':msg,'user':user,'sender':sender}
    
    return render(request,"message_user.html",context)


def delete_messeges(request,id):
    msg=Message.objects.get(message_id = id)
    msg.delete()
    return redirect('/worker_home')

def user_single(request,sender):
    user=User.objects.get(username = sender)
    person=request.session.get('username')
    worker=Worker.objects.get(username=person)
    context={'user':user,'worker':worker}
    if request.method == 'POST':
        reason=request.POST.get('reason')
        report=Report.objects.create(
            user=user,
            reason=reason,
            reported_by=person
        )
        report.save()
    return render(request,"usersingle.html",context) 

def worker_single(request,id):
    username = request.session.get('username')
    user= User.objects.get(username=username )
    worker=Worker.objects.get(username = id)
    context={'user':user,'worker':worker}
    if request.method == 'POST':
        reason=request.POST.get('reason')
        report=Report.objects.create(
            worker=worker,
            reason=reason,
            reported_by=user.username
        )
        report.save()
    return render(request,"workersingle.html",context)

def report_worker(request ,id):
    worker=Worker.objects.get(id = id)
    worker.is_report=True
    worker.save()
    return HttpResponse('worker reported')

def validate_worker(reuest,id):
    worker=Worker.objects.get(id = id)
    worker.is_approved=True
    worker.is_report=False
    worker.save()
    return HttpResponse('worker approved')

def activate_worker(request,id):
    worker=Worker.objects.get(id = id)
    worker.is_report=False
    worker.save()
    return HttpResponse('worker activated')

def mod_worker_single(request,id):
    username = request.session.get('username')
    mod=Moderator.objects.get(username = username)
    worker=Worker.objects.get(id = id)
    context={'mod':mod,'worker':worker}
    return render(request,"mod_workersingle.html",context)


def view_job_progress(request):
    username = request.session.get('username')
    user= User.objects.get(username=username )
    context={'user':user}
    return render(request,"progress.html",context) 