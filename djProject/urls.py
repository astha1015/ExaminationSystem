"""djProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView 
from homepage.views import student_view, logout_view, profile_view, grades_view, agile_test, changeprofile_view 
from homepage.views import course_exams_view, course_grades_view, add_course_view, apply_exam_view, add_exam_view, add_exam_question_view
from login.views import login_view, register_view
from examination.views import add_exam, edit_exam, exam_detail
from django.conf import settings
from django.conf.urls.static import static
from hooks.views import gitlab

urlpatterns = [
    #Admin View
    path('admin/', admin.site.urls),

    #Login views
    path('', LoginView.as_view(), name='login'), #third try.
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),    
    path('register/', register_view, name='register'), 

    #Homepage Views
    path('homepage/', student_view),
    path('profile/', profile_view),
    path('changeprofile/', changeprofile_view, name='changeprofile'),
    path('grades/', grades_view),
    
    path('ag/<exam_id>', agile_test),

    #Course Specific Views
    path('course_exams/<course_id>/',course_exams_view),
    path('course_grades/<course_id>/',course_grades_view),
    path('add_course/', add_course_view),
    path('apply_exam/<course_id>/', apply_exam_view),

    #Exam Views
    path('add_exam/', add_exam_view),
    path('add_exam_question', add_exam_question_view ),
    path('exam<int:pk>/edit/', edit_exam, name='edit_exam'),
    path('exam_detail/', exam_detail ),

    #Webhooks
    path('hooks/', gitlab),

] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
