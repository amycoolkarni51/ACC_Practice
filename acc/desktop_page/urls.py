from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('faq/',views.faq,name='faq'),
    path('faculty/',views.faculty,name='faculty'),
    path('course/',views.course,name='course'),
    path('register/',views.register,name='register'),
    path('success/',views.success,name='success'),
    path('login/',views.login,name='login'),
    path('student_dashboard/',views.student_dashboard,name='student_dashboard'),
    path('course_detail/',views.course_detail,name='course_detail'),
    path('compiler/',views.compiler,name='compiler'),
    path('runcode', views.runcode, name="runcode"),
    path('aboutus', views.aboutus, name="aboutus"),
    
    
]