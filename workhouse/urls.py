"""
URL configuration for workhouse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    
    path('',my_view,name="my_view"),
    path('admin/', admin.site.urls),
    path('admin_worker',admin_worker,name="admin_worker"),
    path('login_view',login_view,name="login_view"),
    path('user_reg',user_reg,name="user_reg"),
    path('worker_reg',worker_reg,name="worker_reg"),
    path('contact_view',contact_view,name="contact_view"),
    path('about_view',about_view,name="about_view"),
    path('my_view',my_view,name="my_view"),
    path('user_home',user_home,name="user_home"),
    path('logout_view',logout_view,name="logout_view"),
    path('worker_home',worker_home,name="worker_home"),
    path('admin_home',admin_home,name="admin_home"),
    path('moderator_home',moderator_home,name="moderator_home"),
    path('job_post',job_post,name="job_post"),
    path('worker_valid',worker_valid,name="worker_valid"),
    path('post_delete/<id>/',post_delete,name="post_delete"),
    path('moderator_delete/<id>',moderator_delete,name="moderator_delete"),
    path('worker_delete/<id>',worker_delete,name="worker_delete"),
    path('status',status,name="status"),
    path('my_radio_view/', my_radio_view, name='my_radio_view'),
    path('job_single/<id>',job_single,name="job_single"),
    path('notify/<id>',notify,name="notify"),
    path('get_notifications/<id>',get_notifications,name="get_notifications"),
    path('send_message/',send_message,name="send_message"),
    path('get_messages/<sender>',get_messages,name="get_messages"),
    path('delete_messeges/<id>',delete_messeges,name="delete_messeges"),
    path('user_single/<sender>',user_single,name="user_single"),
    path('worker_single/<id>',worker_single,name="worker_single"),
    path('report_worker/<id>',report_worker,name="report_worker"),
    path('validate_worker/<id>',validate_worker,name="validate_worker"),
    path('activate_worker/<id>',activate_worker,name="activate_worker"),
    path('get_user_messages/<sender>',get_user_messages,name="get_user_messages"),
    path('send_feedback/',send_feedback,name="send_feedback"),
    path('mod_worker_single/<id>',mod_worker_single,name="mod_worker_single"),
    path('view_job_progress',view_job_progress,name="view_job_progress")


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
