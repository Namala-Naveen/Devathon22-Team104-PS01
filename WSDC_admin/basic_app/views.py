from django.shortcuts import render
import mysql.connector as sql
from .models import display
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
##################################
#taking help of global variable###
##################################
nm=''#for name#
em=''#for email#
paswd=''#for password#
dpmt=''#department#
usrnm=''#forusername#
nam=''#name#
bithdt=''#birthdate#
adh=''#adhar#
add=''#address#
gndr=''#gender#
spclztn=''#specialization#
cat=''#category#
pht=''#photo#
mrksht=''#marksheet#
cstcrt=''#castecertificate#
username=''
password=''
def formpage(request):
    global nm,em,paswd,dpmt
    if request.method=='POST':
        con=sql.connect(host='localhost',user='root',password='Nishant@123',database='wsdc_database')
        cursor=con.cursor()
        object=request.POST
        # grabing all the input data from the respective field #
        for key,value in object.items():
            if key=='name':
                nm=value
            if key=='email':
                em=value
            if key=='password':
                paswd=make_password(value)
            if key=='department':
                dpmt=value
        # starting the sql query #
        qury="insert into admin_2(name,email,password,department) values('{}','{}','{}','{}')".format(nm,em,paswd,dpmt)
        qury1="insert into users_info(name,email,password,department) values('{}','{}','{}','{}')".format(nm,em,paswd,dpmt)
        cursor.execute(qury)
        cursor.execute(qury1)
        con.commit()
    return render(request,'admission.html')

def loginpage(request):
    global usrnm,paswd
    if request.method=='POST':
        con=sql.connect(host='localhost',user='root',password='Nishant@123',database='wsdc_database')
        cursor=con.cursor()
        object=request.POST
        for key,value in object.items():
            if key=='email':
                usrnm=value

            if key=='password':
                paswd=value

        qury="select email,password from users_info where email='{}'and password='{}'".format(usrnm,paswd)
        cursor.execute(qury)
        tur=tuple(cursor.fetchall())
        if tur==():
            return render(request,'error.html')
        else:
            return render(request,'register.html')
        
    return render(request,'intro.html')

def registrationpage(request):
    global nam,bithdt,adh,add,gndr,spclztn,cat,pht,mrksht,cstcrt
    if request.method=='POST':
        con=sql.connect(host='localhost',user='root',password='Nishant@123',database='wsdc_database')
        cursor=con.cursor()
        object=request.POST
        for key,value in object.items():
            if key=='name':
                nam=value
            if key=='birthdate':
                bithdt=value
            if key=='adhaar':
                adh=value
            if key=='address':
                add=value
            if key=='sex':
                gndr=value
            if key=='Specialization':
                spclztn=value
            if key=='image':
                pht=value
            if key=='marksheet':
                mrksht=value
            if key=='casteCertificate':
                cstcrt=value
            if key=='category':
                cat=value
        qury="insert into form_info(name,birthdate,adhaar,address,gender,specialization,category,photo,marksheet,casteCertificate) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(nam,bithdt,adh,add,gndr,spclztn,cat,pht,mrksht,cstcrt)
        cursor.execute(qury)
        con.commit()
        send_mail(
            'testing purpose',
            'thankyou for registering in NITwarangal',
            'nitry929.nikki@gmail.com',
            ['nikaka929@gmail.com'],
            fail_silently=False,
        )
        return render(request,'thankyou.html')

    return render(request,'admission.html')

def adminlogin(request):
    global username,password
    if request.method == 'POST':
        con=sql.connect(host='localhost',user='root',password='Nishant@123',database='wsdc_database')
        cursor=con.cursor()
        object=request.POST
        for key,values in object.items():
            if key=='username':
                username=values
            if key=='password':
                password=values
        qury="select username, password from admin where username='{}' and password='{}'".format(username,password)
        cursor.execute(qury)
        tur=tuple(cursor.fetchall())
        print(f'Tur {tur}')
        if tur==():
            return render(request,'error.html')
        else:
            return adminlist(request)
    return render(request,'adminlogin.html')
            

def adminlist(request):
    data=display.objects.all()
    print('Sufiyan',data)
    return render(request,'adminhome.html',{"displays":data})

def payment(request):
    return render(request,'payment.html')
