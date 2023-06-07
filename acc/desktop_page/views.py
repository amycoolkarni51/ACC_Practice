from django.shortcuts import redirect, render
import mysql.connector as sql
from desktop_page.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def faculty(request):
    return render(request,'faculty.html')

def faq(request):
    return render(request,'faq.html')

def aboutus(request):
    return render(request,'aboutus.html')

def course(request):
    return render(request,'course.html')

def success(request):
    return render(request,'success.html')

def student_dashboard(request):
    return render(request,'student_dashboard.html')

def course_detail(request):
    return render(request,'course_detail.html')

First_Name='',
Last_Name='',
UserName='',
Address='',
Profession='',
Courses='',
EmailId='',
Password='',

def register(request):
    global First_Name,Last_Name,UserName,Address,Profession,Courses,EmailId,Password
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="",database="acc_classes")
        cursor=m.cursor()
        d=request.POST
        
        for key,value in d.items():
            if key=="First_Name":
                First_Name=value
            if key=="Last_Name":
                Last_Name=value
            if key=="UserName":
                UserName=value
            if key=="Address":
                Address=value
            if key=="Profession":
                Profession=value
            if key=="Courses":
                Courses=value
            if key=="EmailId":
                EmailId=value
            if key=="Password":
                Password=value
            if key=="Message":
                Message=value
        
        c="insert into register(First_Name,Last_Name,UserName,Address,Profession,Courses,EmailId,Password,Message) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(First_Name,Last_Name,UserName,Address,Profession,Courses,EmailId,Password,Message)
        cursor.execute(c)
        m.commit()
        return render(request,'index.html')
    return render(request,'register.html')
    
    
def login(request):
    global UserName,EmailId,Password
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="" ,database="acc_classes")
        cursor=m.cursor()
        if request.POST.get("submit")=='Login':
            data=request.POST
            for key,value in data.items():
                if key=='UserName':
                    UserName=value
                if key=='EmailId':
                    EmailId=value
                if key=='Password':
                    Password=value
                          
            query="select * from register where UserName='{}' and EmailId='{}' and Password='{}'".format(UserName,EmailId,Password)  
            cursor.execute(query)
            t=tuple(cursor.fetchall())
            
            if t==():
                return render(request,'register.html') 
            else:
                query2="select * from register where EmailId='{}' and Password='{}'".format(EmailId,Password)
        
                cursor.execute(query2)
                
                result=tuple(cursor.fetchall())
                
                return render(request,'student_dashboard.html',{'result':result}) 
    return render(request,'login.html')


def contact(request):
    if request.method =='POST':
        Full_Name = request.POST['Full_Name']
        EmailId = request.POST['EmailId']
        Subject = request.POST['Subject']
        Message = request.POST['Message']
        
        contact = Contact(Full_Name=Full_Name,EmailId=EmailId,Subject=Subject,Message=Message)
        contact.save()
    return render(request,'contact.html')

import sys
# Create your views here.

def compiler(request):
    return render(request,'compiler.html')

def runcode(request):

    if request.method == "POST":
        codeareadata = request.POST['codearea']

        try:
            #save original standart output reference

            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') #change the standard output to the file we created

            #execute code

            exec(codeareadata)  #example =>   print("hello world")

            sys.stdout.close()

            sys.stdout = original_stdout  #reset the standard output to its original value

            # finally read output from file and save in output variable

            output = open('file.txt', 'r').read()

        except Exception as e:
            # to return error in the code
            sys.stdout = original_stdout
            output = e


    #finally return and render index page and send codedata and output to show on page

    return render(request , 'index.html', {"code":codeareadata , "output":output})

       