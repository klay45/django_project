from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
import json
from django.http import JsonResponse
from django.contrib import messages
from.forms import RegisterUserForm
from.forms import UserUpdateForm
from.forms import ProfileUpdateForm
from.forms import UpdateIDForm
from.forms import DeptandDesignationForm
from.forms import AddIDForm
from django.contrib.auth.forms import UserCreationForm
from .models import Employee
from.models import ID
from .models import Forclaim
from .models import Idcode
from .models import DeptandDesignation
from .models import Idapplication
from .models import AddID
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import random #IDCODE generate
import string #capwords

from tablib import Dataset
from .resources import ForclaimResource
from .resourcesdept import DeptandDesignationResource


import csv
from django.http import FileResponse
from io import BytesIO




def refreshdata(request):
    forclaim=Forclaim.objects.all()
    for item1 in forclaim:
        application=Idapplication.objects.filter(transaction_no=item1.transaction_no).delete()
    return HttpResponseRedirect(reverse('displayid'))




#NEW MODULE FOR ADMIN
def displayidadmin(request):
    #id= ID.objects.all()
    id=AddID.objects.all()
    stat1=Forclaim.objects.all()
    for item in stat1:
        a=int(item.user)
        #b=int(item.transaction_no)
        stat1=ID.objects.filter(user_id=a)and ID.objects.filter(transaction_no=item.transaction_no)
        for item2 in stat1:
            status=item2.status
            print(item2.user_id)
            item2.status="Completed"
            item2.date_printed=item.date_printed
            item2.save()
    context={
    'id1':id1,
    'id':id,
    }

    return render(request,'displayid.html',context)
            
def displayid(request):
    id= ID.objects.all()
    id1=Employee.objects.all()
    stat1=Forclaim.objects.all()
    for item in stat1:
        a=int(item.user)
        #b=int(item.transaction_no)
        stat1=ID.objects.filter(user_id=a)and ID.objects.filter(transaction_no=item.transaction_no)
        for item2 in stat1:
            status=item2.status
            print(item2.user_id)
            item2.status="Completed"
            item2.date_printed=item.date_printed
            item2.save()
    context={
    'id1':id1,
    'id':id,
    }

    return render(request,'displayid.html',context)

def activeapplication(request):
    idapplication = User.objects.all()
    ss=Idapplication.objects.filter(user__in=idapplication)
        
    context={
        'employee':ss
    }
    return render(request,'activeapplication.html',context)

def index(request):
  return render(request,'index.html',{})

def logoutuser(request):
    logout(request)
    messages.success(request,("You Were Log-out!!! "))
    return redirect('index')



def loginuser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request,("Invalid Username or Password"))
            return redirect('loginuser')
            
    else:
        return render(request, 'loginuser.html',{})



def registeruser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        #profile_form = ProfileForm(request.POST) #JULY 21,2022
        #profile_form.user_id=request.user.id
        if form.is_valid():
            reg =form.save(commit=False)
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            a=string.capwords(first_name)
            b=string.capwords(last_name)
            reg.first_name=a
            reg.last_name=b
            reg.save()
            


            #form.save()
            #profile_form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request,("Registration Successful!"))
            return redirect('index')
    else:
        form = RegisterUserForm()
        #profile_form = ProfileForm()
    return render(request,'registeruser.html',{'form':form},)



@login_required(login_url='loginuser')
def status(request):
    status = ID.objects.filter(user=request.user)
    status1 = Employee.objects.filter(user=request.user)

    context= {
        'status':status,
        'status1':status1
    }

    return render(request,"status.html",context)
    

    """if not Forclaim.objects.filter(user=request.user.id):
        context = {
        'status':status,
        'status1':status1,
    
        }

        return render(request,"status.html",context)
    else:
        q= Forclaim.objects.filter(user=request.user.id)
        for item in q:
            for item1 in status:    
                print('pass')
    

        a=int(item.user)
        b=item1.user_id

       
        member = ID.objects.get(user_id=a)        
        c=item.date_printed
        #c=item.date_printed
        if (a==b):
        
            member.status="Completed"
            member.date_printed=c
            
            #print(member.status)
            member.save()
            status2 = ID.objects.filter(user=request.user)
            status11 = Employee.objects.filter(user=request.user)
            
            context = {
            'status':status2,
            'status1':status11,
    
            }

    
            return render(request,"status.html",context)"""


def downloadidadmin(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=ID_Application.csv'
    writer= csv.writer(response)
    user = AddID.objects.all()
    
    writer.writerow(['User ID','Full Name','Designation','ID Code','Birth Date','Address','Contact Person','Contact Person Address','Contact Number','Pictures','Signature','Barcode','SSS No.','TIN','Blood Type','ID Status','Employee Contact Number','Transaction No.'])
    for item in user:
        #details = Employee.objects.filter(user_id = item.id)
        #for item1 in details:
            #foridapplication=Idapplication.objects.filter(user_id=item1.user_id)
            #for item2 in foridapplication:
        a=item.midle_initial
        a1=a[0]
        b=str(item.id_pic)
        c=("\\"+chr(92)+"192.168.6.87"+chr(92)+"Users"+chr(92)+"epcc"+chr(92)+"epccid"+chr(92)+"media"+chr(92))
        d=str(item.signature)
        firstname=str(item.first_name)

        writer.writerow([item.id,firstname+" "+a1+". "+item.last_name+" "+item.name_extension,item.disignation,item.id_code,item.birth_date,item.address,item.contact_person,item.contact_person_address,item.contact_person_no,c+ b,c+d,"",item.sss_no,item.tin,item.blood_type,"",item.contact_person_no,item.transaction_no])


            
    return response








def downloadidapp(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=ID_Application.csv'
    writer= csv.writer(response)
    user = User.objects.all()
    
    writer.writerow(['User ID','Full Name','Designation','ID Code','Birth Date','Address','Contact Person','Contact Person Address','Contact Number','Pictures','Signature','Barcode','SSS No.','TIN','Blood Type','ID Status','Employee Contact Number','Transaction No.'])
    for item in user:
        details = Employee.objects.filter(user_id = item.id)
        for item1 in details:
            foridapplication=Idapplication.objects.filter(user_id=item1.user_id)
            for item2 in foridapplication:
                a=item1.midle_initial
                a1=a[0]
                b=str(item1.id_pic)
                c=("\\"+chr(92)+"192.168.6.87"+chr(92)+"Users"+chr(92)+"epcc"+chr(92)+"epccid"+chr(92)+"media"+chr(92))
                d=str(item1.signature)
                firstname=str(item.first_name)

                writer.writerow([item.id,firstname+" "+a1+". "+item.last_name+" "+item1.name_extension,item1.disignation,item1.id_code,item1.birth_date,item1.address,item1.contact_person,item1.contact_person_address,item1.contact_person_no,c+ b,c+d,"",item1.sss_no,item1.tin,item1.blood_type,"",item1.contact_person_no,item2.transaction_no])


            
    return response



#for admin module
def importidforclaimadmin(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        fish_resource = ForclaimResource()
        f=ForclaimAdmin.objects.all()
        dataset = Dataset()
        new_fish = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_fish.read().decode('utf-8'),format='csv')
            result = fish_resource.import_data(dataset, dry_run=True)   
            

          

        elif file_format == 'JSON':
            imported_data = dataset.load(new_fish.read().decode('utf-8'),format='json')
            # Testing data import
            result = fish_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            # Import now
            fish_resource.import_data(dataset, dry_run=False)



    return render(request, 'importadmin.html')








def importidforclaim(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        fish_resource = ForclaimResource()
        f=Forclaim.objects.all()
        dataset = Dataset()
        new_fish = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_fish.read().decode('utf-8'),format='csv')
            result = fish_resource.import_data(dataset, dry_run=True)   
            

          

        elif file_format == 'JSON':
            imported_data = dataset.load(new_fish.read().decode('utf-8'),format='json')
            # Testing data import
            result = fish_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            # Import now
            fish_resource.import_data(dataset, dry_run=False)



    return render(request, 'import.html')


def importdeptanddesignation(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        fish_resource = DeptandDesignationResource()
        #f=Forclaim.objects.all()
        dataset = Dataset()
        new_fish = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_fish.read().decode('utf-8'),format='csv')
            result = fish_resource.import_data(dataset, dry_run=True)   
           
            print(dataset)
          

        elif file_format == 'JSON':
            imported_data = dataset.load(new_fish.read().decode('utf-8'),format='json')
            # Testing data import
            result = fish_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            # Import now
            fish_resource.import_data(dataset, dry_run=False)

    return render(request, 'importdeptanddesignation.html')


def updateremarks(request, id):
    submitted = False
    if request.method == 'POST':


        fish = ID.objects.get(user_id=id)
        fish_form = UpdateIDForm(request.POST,request.FILES,instance=fish)

    
        if fish_form.is_valid():
            fish_form.save()
           
            messages.success(request,f'Successfully Add Remarks')
            return redirect('buy')
    else:
            fish = ID.objects.get(user_id=id)       
            fish_form = UpdateIDForm(instance=fish)

           
    fish = ID.objects.get(user_id=id)
    context= {
        'fish_form':fish_form
        
        
    }

    return render(request,'updateremarks.html',context)


def updateremarks1(request, id):
    mymember = ID.objects.get(id=id)
    template = loader.get_template('updateremarks1.html')
    context ={
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request,id):
    #first = request.POST['first']
    remarks = request.POST['remarks']
    member = ID.objects.get(id=id)
    member.remarks = remarks
    
    member.save()
    return HttpResponseRedirect(reverse('displayid'))


def searchidapplication(request):
    if request.method == "POST":
        searched = request.POST['searched']
        h=string.capwords(searched)
       
        idapplication = User.objects.filter(first_name__contains=h)or User.objects.filter(last_name__contains=h)
        ss=ID.objects.filter(user__in=idapplication)
        
        context={
            'idapplication':ss
        }
        return render(request,'searchidapplication.html',context)
    else:
        return render(request,'searchidapplication.html',{})





def addid(request):
    submitted = False
    if request.method == "POST":
        id_form = AddIDForm(request.POST,request.FILES)


        #if form.is_valid():
           # form.save()
            #return HttpResponseRedirect('/addfish2?submitted=True')
            #return HttpResponseRedirect(reverse('buy'))
            #return HttpResponseRedirect('/addfish2')


        print('sulod')
        if id_form.is_valid():
                print('next sulod')

                
                post = id_form.save(commit=False)
                #post1= u_form.save(commit=False)
                data = id_form.cleaned_data
                #data1=u_form.cleaned_data
                id_code = data['id_code']


                first_name=data['first_name']
                midle_initial=data['midle_initial']
                name_extension=data['name_extension']
                a=string.capwords(midle_initial)
                a1=a[0]
                last_name=data['last_name']
                name=first_name+" "+a1+"."+" "+last_name+name_extension
                print(name)
                oldname=DeptandDesignation.objects.filter(fullname=name)
                print(oldname)




                trans_no='klay45'+str(random.randint(1111111,9999999))
                while ID.objects.filter(transaction_no=trans_no)is None:
                    track='klay45'+str(random.randint(1111111,9999999))
                #id_application.transaction_no=trans_no

                
                if id_code == "":
                    
                    
                    data=id_form.cleaned_data
                    
                    designation = data['disignation']
                    print("pass de")


                    if DeptandDesignation.objects.filter(fullname=name):
                        print(name)

                        oldname=DeptandDesignation.objects.filter(fullname=name)
                        for nn in oldname:
                            print(nn.fullname)

                        contact_person_address=data['contact_person_address']
                        midle_initial=data['midle_initial']
                        address=data['address']
                        name_extension=data['name_extension']
                        contact_person=data['contact_person']
                        #blood_type=data['blood_type']
                        first_name=data['first_name']
                        last_name=data['last_name']


                        a=string.capwords(contact_person_address)
                        b=string.capwords(midle_initial)
                        c=string.capwords(address)
                        d=string.capwords(name_extension)
                        e=string.capwords(contact_person)
                        #f=string.capwords(blood_type)
                        g=string.capwords(first_name)
                        h=string.capwords(last_name)


                        post.id_code = nn.idcode
                        post.first_name=g
                        post.last_name=h
                        post.contact_person_address=a
                        post.midle_initial=b
                        post.address=c
                        post.name_extension=d
                        post.contact_person=e
                        #post.blood_type=f
                        post.first_name=g
                        post.last_name=h
                        post.transaction_no=trans_no
                        #print("trans_no")

                        post.save()
                        #post1.save()

                        #id_application.save()
                        messages.success(request,f'Successfully Apply for ID SHIT')
                        return redirect('status')



                    else:
                        if designation =="IT Staff" or designation=="IT Technician" or designation=="OIC, MIS Section":

                            idcode=Idcode()
                            idcode.department="MIS"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="MIS").latest('id_code')
                        #aa=Idcode.objects.filter() #and (Idcode.objects.latest('id_code')))
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="EPCC-MIS-0"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code


                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            #blood_type=data['blood_type']
                            first_name=data['first_name']
                            last_name=data['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            #f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            #post.blood_type=f
                            post.first_name=g
                            post.last_name=h
                            post.transaction_no=trans_no

                            post.save()
                            #post1.save()
                            #print(id_application.employee)

                            #id_application.save()
                            messages.success(request,f'Successfully Apply for ID SHIT IT')
                  

                            return redirect('status')

                        elif designation =="Service Driver" or designation=="Backhoe Operator" or designation=="Forklift Operator"or designation=="Aircon Technician" or designation=="Apprentice Auto-Electrician" or designation=="Asphalt Distributor Operator"or designation=="Asphalt Paver Operator"or designation=="Associate Area Supervisor"or designation=="Auto Aircon Electrician"or designation=="Auto Electrician"or designation=="Auto Paintor"or designation=="Backhoe Operator"or designation=="Barge Tender"or designation=="Battery Man"or designation=="Boat Captain"or designation=="Body Builder"or designation=="Boomtruck Driver"or designation=="Bulldozer Operator" or designation=="Calibrator Operator"or designation=="Canvasser"or designation=="Chief Mate"or designation=="Cold Milling Machine Operator"or designation=="Concrete Paver Operator"or designation=="Concrete Pumpcrete Operator"or designation=="Concrete Pumptruck Operator"or designation=="Crane Operator"or designation=="Crimping Machine Operator"or designation=="Diesel Hammer Operator"or designation=="Dumptruck Driver"or designation=="Electrical Section Supervisor"or designation=="Electrician"or designation=="Electronic Technician"or designation=="Equipment And Rental Billing Analyst"or designation=="Equipment Coordinator"or designation=="Equipment History Analyst"or designation=="Equipment Management Analyst"or designation=="Equipment Management Area Supervisor"or designation=="Equipment Monitoring Processor"or designation=="Equipment Rental Billing Analyst"or designation=="Equipment Service Analyst R13"or designation=="Equipment Service Processor"or designation=="Fuel Tanker Driver"or designation=="Generator Technician"or designation=="Helper"or designation=="Helper - Machine Shop"or designation=="Hydraulic Hammer Operator"or designation=="Industrial Electrician"or designation=="Junior Mechanic"or designation=="Leadman"or designation=="Lubeman"or designation=="Machine Shop Section Supervisor"or designation=="Machinist"or designation=="Machinist Helper"or designation=="Marine Equipment In-Charge"or designation=="Mini-Fuel Tanker Driver"or designation=="Mechanical Section Supervisor"or designation=="Mini-Dumptruck Driver"or designation=="Chief Mate"or designation=="Motorpool Maintenance Personnel"or designation=="Motorpool Supervisor (Iligan)"or designation=="Motorpool Technician"or designation=="Office Aide"or designation=="Painter"or designation=="Payloader Operator"or designation=="Permits And Licensing Officer"or designation=="Power Tool Technician"or designation=="Preventive Maintenance Compliance Officer"or designation=="Prime Mover Driver"or designation=="Pumpboat Operator"or designation=="Quarter Master"or designation=="Radiator Maintenance"or designation=="Refinery Machine Operator"or designation=="Rigger"or designation=="Road Grader Operator"or designation=="Road Roller Operator"or designation=="Self Loader Driver"or designation=="Senior Electrician"or designation=="Service Advisor"or designation=="Service Advisor Processor"or designation=="Service Driver"or designation=="Shuttle Bus Driver"or designation=="Stake Truck Driver"or designation=="Tender"or designation=="Tireman"or designation=="Transit Mixer Driver"or designation=="Vibro Hammer Operator"or designation=="Water Truck Driver"or designation=="Welder"or designation=="Welding Section Supervisor":
                        #code ='EMD'+str(random.randint(1111111,9999999))

                            idcode=Idcode()
                            idcode.department="EMD"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="EMD").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="OPR-EMD-"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code


                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data['first_name']
                            last_name=data['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post.first_name=g
                            post.last_name=h
                            post.transaction_no=trans_no

                            post.save()
                            #post1.save()
                            #id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')
                            




                        elif designation =="Drilling Operator" or designation=="Field Engineer" or designation=="Geodetic Engineer"or designation=="Instrument Man"or designation=="Junior Project Manager"or designation=="Office Assistant"or designation=="Paving Block Operator/In-Charge"or designation=="Project Accounting Processor"or designation=="Project Accounting Supervisor"or designation=="Project Engineer"or designation=="Project Processor"or designation=="Survey Aide"or designation=="Surveyor":
                        #code ='EMD'+str(random.randint(1111111,9999999))

                            idcode=Idcode()
                            idcode.department="PMD"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="PMD").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="OPR-ENG-"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data['first_name']
                            last_name=data['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post.first_name=g
                            post.last_name=h
                            post.transaction_no=trans_no

                            post.save()
                            #post1.save()
                            #id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')


                        elif designation =="Company Nurse"or designation=="Project Nurse" or designation=="First Aider" or designation=="Safety And Health Division Head"or designation=="Safety And Health Processor"or designation=="Safety Officer"or designation=="Administrative Support Processor"or designation=="Billing Processor"or designation=="GPS/CCTV Maintenance"or designation=="GSD Processor"or designation=="Internal Security"or designation=="Office Utility"or designation=="OIC, Facilities Maintenance Section"or designation=="Permits And Licenses Processor"or designation=="Records Custodian"or designation=="Security Processor"or designation=="Security Section Supervisor"or designation=="Tarpaulin Production Assistant"or designation=="Truck Master":
                            idcode=Idcode()
                            idcode.department="GSD"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="GSD").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="ADM-GSD-"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data['first_name']
                            last_name=data['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post.first_name=g
                            post.last_name=h
                            post.transaction_no=trans_no

                            post.save()
                            #post1.save()
                            #id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')



                        elif designation =="Accounting Analyst" or designation=="Accounting Processor" or designation=="Accounts Payable Billing Processor"or designation=="Accounts Payable Clerk II"or designation=="Accounts Payable Disbursement Clerk II"or designation=="Administrative Support Processor"or designation=="Accounts Payable Section Supervisor R13"or designation=="Accounts Receivable Processor"or designation=="Accounts Receivables Section Supervisor"or designation=="AP Billing Bookkeeper"or designation=="AP Billing Clerk"or designation=="AP Billing Processor"or designation=="AP Disbursement Bookkeeper"or designation=="AP Disbursement Clerk"or designation=="AP Disbursement Clerk (Aide)"or designation=="AP Disbursement Processor"or designation=="Asset Account Processor"or designation=="Bookkeeper"or designation=="Bookkeeper III"or designation=="Compliance Bookkeeper"or designation=="Compliance Clerk II"or designation=="Disbursement Clerk"or designation=="Disbursement Clerk II"or designation=="OIC, Accounts Payable Section R10"or designation=="Reconciliation Processor":
                            idcode=Idcode()
                            idcode.department="Accounting"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="Accounting").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="FIN-ACT-"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data['first_name']
                            last_name=data['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post.first_name=g
                            post.last_name=h
                            post.transaction_no=trans_no

                            post.save()
                            #post1.save()
                            #id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')


                        elif designation =="Collection Processor" or designation=="Collection Section Supervisor" or designation=="Disbursement And Collection Processor"or designation=="Disbursement And Collection Supervisor"or designation=="Disbursement Processor"or designation=="Disbursing Supervisor R10"or designation=="Disbursing Supervisor R13"or designation=="Office Cashier"or designation=="Treasury Aide"or designation=="Treasury Processor":
                            idcode=Idcode()
                            idcode.department="Treasury"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="Treasury").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="FIN-TRE-"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data['first_name']
                            last_name=data['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post.first_name=g
                            post.last_name=h
                            post.transaction_no=trans_no

                            post.save()
                            #post1.save()
                            #id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')


                        elif designation =="Compensation And Benefits Processor" or designation=="Employee Relations Processor" or designation=="HR Assistant"or designation=="Human Resource Generalist"or designation=="OIC, Compensation And Benefits Section"or designation=="OIC, Employee Relations Section"or designation=="Records In-Charge"or designation=="Recruitment And Hiring Processor"or designation=="Recruitment And Hiring Section Supervisor"or designation=="Training And Development Section Supervisor"or designation=="Training Associate":
                            idcode=Idcode()
                            idcode.department="Human Resource"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="Human Resource").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="ADM-HRD-"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data['first_name']
                            last_name=data['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post.first_name=g
                            post.last_name=h
                            post.transaction_no=trans_no

                            post.save()
                            #post1.save()
                            #id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')



                        elif designation =="Gasman" or designation=="Inventory Management Requisition Analyst" or designation=="Inventory Withdrawal Processor"or designation=="Stock Analyst"or designation=="IMD Reception"or designation=="Inventory Management Withdrawal Analyst (Central/Project)"or designation=="Inventory Variance Report Processor"or designation=="Toolkeeper"or designation=="IMD-Junior Parts Specialist"or designation=="OIC, Inventory Management Section 13"or designation=="Inventory Management Stock Analyst"or designation=="Materials Receiving Processor"or designation=="Inventory Management Withdrawal Analyst (Project)"or designation=="Inventory Management Parts Specialist"or designation=="Lube Stockman"or designation=="Inventory Management Withdrawal Encoder - Central"or designation=="Inventory Management Receiving Analyst"or designation=="Inventory Management Control Specialist"or designation=="Inventory Management Processor"or designation=="Inventory Control Specialist"or designation=="Inventory Management Receiving Analyst (Project)"or designation=="OIC, Inventory Management Section R10"or designation=="Receiving Analyst"or designation=="Warehouse Tender"or designation=="Inventory Management Withdrawal Analyst":
                            idcode=Idcode()
                            idcode.department="IMD"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="IMD").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="ADM-IMD-"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data['first_name']
                            last_name=data['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post.first_name=g
                            post.last_name=h
                            post.transaction_no=trans_no

                            post.save()
                            #post1.save()
                            #id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')

                        elif designation =="Bidding And Contracts Officer" or designation =="Bidding And Contracts Processor" or designation =="Contract Handling Processor" or designation =="Marketing Aide" or designation =="Office Engineer" or designation =="OIC, Contracts And Handling Section" or designation =="OIC, Special License Handling Section" or designation =="Special License Compliance Processor":
                            idcode=Idcode()
                            idcode.department="Marketing"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="Marketing").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="MTG-MBD-0"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data['first_name']
                            last_name=data['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post.first_name=g
                            post.last_name=h
                            post.transaction_no=trans_no

                            post.save()
                            #post1.save()
                            #id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')


                        elif designation =="Billing Aide" or designation =="Billing Officer" or designation =="Billing Section Supervisor R10" or designation =="Cadd Operator" or designation =="Civil 3D Operator" or designation =="Cost Engineer" or designation =="Monitoring Engineer" or designation =="OIC, Billing Section R13" or designation =="Project Monitoring Section Supervisor" or designation =="Quantity Engineer" or designation =="Technical Assistant" or designation =="Technical Engineer" or designation =="Technical Officer" or designation =="Technical Services Processor":
                            idcode=Idcode()
                            idcode.department="TSD"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="TSD").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="ENG-TSD-0"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data['first_name']
                            last_name=data['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post.first_name=g
                            post.last_name=h
                            post.transaction_no=trans_no

                            post.save()
                            #post1.save()
                            #id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')


                        elif designation =="Canvassing Processor"or designation =="Purchaser" or designation =="Procurement Processor" or designation =="Purchasing Processor" or designation =="Records Processor" or designation =="OIC, Canvassing Division R13" or designation =="OIC, Canvassing Section R10" or designation =="PO Processor" or designation =="Procurement Analyst R10" or designation =="Canvassing Proccesor" or designation =="Turn-Over Processor" or designation =="Procurement Analyst R13" or designation =="OIC, Logistics Section R13" or designation =="Canvassing Processor R13" or designation =="Procurement Processor R13":
                            idcode=Idcode()
                            idcode.department="PROCUREMENT"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="PROCUREMENT").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="ADM-LOG-"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data['first_name']
                            last_name=data['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post.first_name=g
                            post.last_name=h
                            post.transaction_no=trans_no

                            post.save()
                            #post1.save()
                            #id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')



                        elif designation =="Accounting And Recording Audit Supervisor" or designation =="Document Controller" or designation =="Document Custodian" or designation =="Field Auditor" or designation =="Internal Audit System Assistant" or designation =="Internal Control Financial Reporting Division Head" or designation =="OIC, IAS QMS Section" or designation =="QMS Assistant":
                            idcode=Idcode()
                            idcode.department="IAS"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="IAS").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="IAS-QMS-0"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data['first_name']
                            last_name=data['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post.first_name=g
                            post.last_name=h
                            post.transaction_no=trans_no

                            post.save()
                            #post1.save()
                            #id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')


                        elif designation =="Asphalt Heating Operator" or designation =="Assistant Plant Operator"or designation =="Checker"or designation =="Clerical Processor"or designation =="Compliance Section Supervisor"or designation =="Foreman"or designation =="Heating Operator"or designation =="Mining Engineer"or designation =="Plant Account Analyst"or designation =="Plant Aide"or designation =="Plant Electrician"or designation =="Plant Maintenance"or designation =="Plant Operator"or designation =="Plant Processor"or designation =="Plant Supervisor"or designation =="Plant Technician"or designation =="Plants Processor"or designation =="Project Cashier"or designation =="Project Safety Aide"or designation =="Social Development Officer"or designation =="Truckscale Operator":
                            idcode=Idcode()
                            idcode.department="Production"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="Production").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="OPR-PROD-0"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data['first_name']
                            last_name=data['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post.first_name=g
                            post.last_name=h
                            post.transaction_no=trans_no

                            post.save()
                            #post1.save()
                            #id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')



                        elif designation =="Chemical Laboratory Supervisor" or designation =="Chemist" or designation =="Laboratory Aide" or designation =="Laboratory Technician" or designation =="Materials Assistant" or designation =="Materials Engineer" or designation =="Physical Labortory Supervisor" or designation =="Quality Control Engineer":
                            idcode=Idcode()
                            idcode.department="Materials Quality Control"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="Materials Quality Control").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="OPR-QC-0"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data['first_name']
                            last_name=data['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)



                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post.first_name=g
                            post.last_name=h
                            post.transaction_no=trans_no

                            post.save()
                            #post1.save()
                            #id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')

                else:
                    if not DeptandDesignation.objects.filter(fullname=name):

                        contact_person_address=data['contact_person_address']
                        midle_initial=data['midle_initial']
                        address=data['address']
                        name_extension=data['name_extension']
                        contact_person=data['contact_person']
                        blood_type=data['blood_type']
                        first_name=data['first_name']
                        last_name=data['last_name']


                        a=string.capwords(contact_person_address)
                        b=string.capwords(midle_initial)
                        c=string.capwords(address)
                        d=string.capwords(name_extension)
                        e=string.capwords(contact_person)
                        f=string.capwords(blood_type)
                        g=string.capwords(first_name)
                        h=string.capwords(last_name)
                        print("walay match")
                        print(name)

                        post.first_name=g
                        post.last_name=h
                        post.contact_person_address=a
                        post.midle_initial=b
                        post.address=c
                        post.name_extension=d
                        post.contact_person=e
                        post.blood_type=f
                        post.first_name=g
                        post.last_name=h
                        post.transaction_no=trans_no

                        post.save()
                        #post1.save()

                        #id_application.save()
                        messages.success(request,f'Successfully Apply for ID SHIT')
                        return redirect('status')

                    else:

                        oldname=DeptandDesignation.objects.filter(fullname=name)
                        for nn in oldname:
                                print(nn.fullname)

                        contact_person_address=data['contact_person_address']
                        midle_initial=data['midle_initial']
                        address=data['address']
                        name_extension=data['name_extension']
                        contact_person=data['contact_person']
                        blood_type=data['blood_type']
                        first_name=data['first_name']
                        last_name=data['last_name']


                        a=string.capwords(contact_person_address)
                        b=string.capwords(midle_initial)
                        c=string.capwords(address)
                        d=string.capwords(name_extension)
                        e=string.capwords(contact_person)
                        f=string.capwords(blood_type)
                        g=string.capwords(first_name)
                        h=string.capwords(last_name)

                        post.id_code = nn.idcode
                        post.first_name=g
                        post.last_name=h
                        post.contact_person_address=a
                        post.midle_initial=b
                        post.address=c
                        post.name_extension=d
                        post.contact_person=e
                        post.blood_type=f
                        post.first_name=g
                        post.last_name=h
                        post.transaction_no=trans_no

                        post.save()
                        #post1.save()


                        #id_application.save()
                        messages.success(request,f'Successfully Apply for ID SHIT')
                        return redirect('status')




    else:
        id_form = AddIDForm()
        #id_form = AddIDForm(request.POST,request.FILES)

    context= {
        'id_form':id_form,
   
    }

    return render(request,'addid.html',context)


@login_required(login_url='loginuser')
def profile(request):
    submitted = False
    if request.method == 'POST':

        if not Employee.objects.filter(user=request.user.id):
            employee = Employee()
            employee.user_id = request.user.id
            id_application= ID()
            id_application.user = request.user


            trans_no='klay45'+str(random.randint(1111111,9999999))
            while ID.objects.filter(transaction_no=trans_no)is None:
                track='klay45'+str(random.randint(1111111,9999999))
            id_application.transaction_no=trans_no
            
            
            u_form = UserUpdateForm(request.POST,instance=request.user)
            p_form = ProfileUpdateForm(request.POST,request.FILES, instance=employee)


            if not Idapplication.objects.filter(user=request.user):
                foridapplication=Idapplication()
                foridapplication.user=request.user

                foridapplication.transaction_no=trans_no
                foridapplication.save()





            if p_form.is_valid() and u_form.is_valid():

                
                post = p_form.save(commit=False)
                post1= u_form.save(commit=False)
                data = p_form.cleaned_data
                data1=u_form.cleaned_data
                id_code = data['id_code']


                first_name=data1['first_name']
                midle_initial=data['midle_initial']
                name_extension=data['name_extension']
                a=string.capwords(midle_initial)
                a1=a[0]
                last_name=data1['last_name']
                name=first_name+" "+a1+"."+" "+last_name+" "+name_extension
                oldname=DeptandDesignation.objects.filter(fullname=name)
                print(oldname)

                
                if id_code == "":
                    
                    
                    data1=u_form.cleaned_data
                    
                    designation = data['disignation']
                    print("pass")


                    if DeptandDesignation.objects.filter(fullname=name):

                        oldname=DeptandDesignation.objects.filter(fullname=name)
                        for nn in oldname:
                            print(nn.fullname)

                        contact_person_address=data['contact_person_address']
                        midle_initial=data['midle_initial']
                        address=data['address']
                        name_extension=data['name_extension']
                        contact_person=data['contact_person']
                        #blood_type=data['blood_type']
                        first_name=data1['first_name']
                        last_name=data1['last_name']


                        a=string.capwords(contact_person_address)
                        b=string.capwords(midle_initial)
                        c=string.capwords(address)
                        d=string.capwords(name_extension)
                        e=string.capwords(contact_person)
                        #f=string.capwords(blood_type)
                        g=string.capwords(first_name)
                        h=string.capwords(last_name)


                        post.id_code = nn.idcode
                        post.first_name=g
                        post.last_name=h
                        post.contact_person_address=a
                        post.midle_initial=b
                        post.address=c
                        post.name_extension=d
                        post.contact_person=e
                        #post.blood_type=f
                        post1.first_name=g
                        post1.last_name=h

                        post.save()
                        post1.save()

                        id_application.save()
                        messages.success(request,f'Successfully Apply for ID SHIT')
                        return redirect('status')



                    else:
                        if designation =="IT Staff" or designation=="IT Technician" or designation=="OIC, MIS Section":

                            idcode=Idcode()
                            idcode.department="MIS"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="MIS").latest('id_code')
                        #aa=Idcode.objects.filter() #and (Idcode.objects.latest('id_code')))
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="EPCC-MIS-0"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code


                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            #blood_type=data['blood_type']
                            first_name=data1['first_name']
                            last_name=data1['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            #f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            #post.blood_type=f
                            post1.first_name=g
                            post1.last_name=h

                            post.save()
                            post1.save()
                            #print(id_application.employee)

                            id_application.save()
                            messages.success(request,f'Successfully Apply for ID SHIT IT')
                  

                            return redirect('status')

                        elif designation =="Service Driver" or designation=="Backhoe Operator" or designation=="Forklift Operator"or designation=="Aircon Technician" or designation=="Apprentice Auto-Electrician" or designation=="Asphalt Distributor Operator"or designation=="Asphalt Paver Operator"or designation=="Associate Area Supervisor"or designation=="Auto Aircon Electrician"or designation=="Auto Electrician"or designation=="Auto Paintor"or designation=="Backhoe Operator"or designation=="Barge Tender"or designation=="Battery Man"or designation=="Boat Captain"or designation=="Body Builder"or designation=="Boomtruck Driver"or designation=="Bulldozer Operator" or designation=="Calibrator Operator"or designation=="Canvasser"or designation=="Chief Mate"or designation=="Cold Milling Machine Operator"or designation=="Concrete Paver Operator"or designation=="Concrete Pumpcrete Operator"or designation=="Concrete Pumptruck Operator"or designation=="Crane Operator"or designation=="Crimping Machine Operator"or designation=="Diesel Hammer Operator"or designation=="Dumptruck Driver"or designation=="Electrical Section Supervisor"or designation=="Electrician"or designation=="Electronic Technician"or designation=="Equipment And Rental Billing Analyst"or designation=="Equipment Coordinator"or designation=="Equipment History Analyst"or designation=="Equipment Management Analyst"or designation=="Equipment Management Area Supervisor"or designation=="Equipment Monitoring Processor"or designation=="Equipment Rental Billing Analyst"or designation=="Equipment Service Analyst R13"or designation=="Equipment Service Processor"or designation=="Fuel Tanker Driver"or designation=="Generator Technician"or designation=="Helper"or designation=="Helper - Machine Shop"or designation=="Hydraulic Hammer Operator"or designation=="Industrial Electrician"or designation=="Junior Mechanic"or designation=="Leadman"or designation=="Lubeman"or designation=="Machine Shop Section Supervisor"or designation=="Machinist"or designation=="Machinist Helper"or designation=="Marine Equipment In-Charge"or designation=="Mini-Fuel Tanker Driver"or designation=="Mechanical Section Supervisor"or designation=="Mini-Dumptruck Driver"or designation=="Chief Mate"or designation=="Motorpool Maintenance Personnel"or designation=="Motorpool Supervisor (Iligan)"or designation=="Motorpool Technician"or designation=="Office Aide"or designation=="Painter"or designation=="Payloader Operator"or designation=="Permits And Licensing Officer"or designation=="Power Tool Technician"or designation=="Preventive Maintenance Compliance Officer"or designation=="Prime Mover Driver"or designation=="Pumpboat Operator"or designation=="Quarter Master"or designation=="Radiator Maintenance"or designation=="Refinery Machine Operator"or designation=="Rigger"or designation=="Road Grader Operator"or designation=="Road Roller Operator"or designation=="Self Loader Driver"or designation=="Senior Electrician"or designation=="Service Advisor"or designation=="Service Advisor Processor"or designation=="Service Driver"or designation=="Shuttle Bus Driver"or designation=="Stake Truck Driver"or designation=="Tender"or designation=="Tireman"or designation=="Transit Mixer Driver"or designation=="Vibro Hammer Operator"or designation=="Water Truck Driver"or designation=="Welder"or designation=="Welding Section Supervisor":
                        #code ='EMD'+str(random.randint(1111111,9999999))

                            idcode=Idcode()
                            idcode.department="EMD"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="EMD").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="OPR-EMD-"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code


                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data1['first_name']
                            last_name=data1['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post1.first_name=g
                            post1.last_name=h

                            post.save()
                            post1.save()
                            id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')
                            




                        elif designation =="Drilling Operator" or designation=="Field Engineer" or designation=="Geodetic Engineer"or designation=="Instrument Man"or designation=="Junior Project Manager"or designation=="Office Assistant"or designation=="Paving Block Operator/In-Charge"or designation=="Project Accounting Processor"or designation=="Project Accounting Supervisor"or designation=="Project Engineer"or designation=="Project Processor"or designation=="Survey Aide"or designation=="Surveyor":
                        #code ='EMD'+str(random.randint(1111111,9999999))

                            idcode=Idcode()
                            idcode.department="PMD"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="PMD").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="OPR-ENG-"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data1['first_name']
                            last_name=data1['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post1.first_name=g
                            post1.last_name=h

                            post.save()
                            post1.save()
                            id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')


                        elif designation =="Company Nurse"or designation=="Project Nurse" or designation=="First Aider" or designation=="Safety And Health Division Head"or designation=="Safety And Health Processor"or designation=="Safety Officer"or designation=="Administrative Support Processor"or designation=="Billing Processor"or designation=="GPS/CCTV Maintenance"or designation=="GSD Processor"or designation=="Internal Security"or designation=="Office Utility"or designation=="OIC, Facilities Maintenance Section"or designation=="Permits And Licenses Processor"or designation=="Records Custodian"or designation=="Security Processor"or designation=="Security Section Supervisor"or designation=="Tarpaulin Production Assistant"or designation=="Truck Master":
                            idcode=Idcode()
                            idcode.department="GSD"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="GSD").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="ADM-GSD-"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data1['first_name']
                            last_name=data1['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post1.first_name=g
                            post1.last_name=h

                            post.save()
                            post1.save()
                            id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')



                        elif designation =="Accounting Analyst" or designation=="Accounting Processor" or designation=="Accounts Payable Billing Processor"or designation=="Accounts Payable Clerk II"or designation=="Accounts Payable Disbursement Clerk II"or designation=="Administrative Support Processor"or designation=="Accounts Payable Section Supervisor R13"or designation=="Accounts Receivable Processor"or designation=="Accounts Receivables Section Supervisor"or designation=="AP Billing Bookkeeper"or designation=="AP Billing Clerk"or designation=="AP Billing Processor"or designation=="AP Disbursement Bookkeeper"or designation=="AP Disbursement Clerk"or designation=="AP Disbursement Clerk (Aide)"or designation=="AP Disbursement Processor"or designation=="Asset Account Processor"or designation=="Bookkeeper"or designation=="Bookkeeper III"or designation=="Compliance Bookkeeper"or designation=="Compliance Clerk II"or designation=="Disbursement Clerk"or designation=="Disbursement Clerk II"or designation=="OIC, Accounts Payable Section R10"or designation=="Reconciliation Processor":
                            idcode=Idcode()
                            idcode.department="Accounting"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="Accounting").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="FIN-ACT-"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data1['first_name']
                            last_name=data1['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post1.first_name=g
                            post1.last_name=h

                            post.save()
                            post1.save()
                            id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')


                        elif designation =="Collection Processor" or designation=="Collection Section Supervisor" or designation=="Disbursement And Collection Processor"or designation=="Disbursement And Collection Supervisor"or designation=="Disbursement Processor"or designation=="Disbursing Supervisor R10"or designation=="Disbursing Supervisor R13"or designation=="Office Cashier"or designation=="Treasury Aide"or designation=="Treasury Processor":
                            idcode=Idcode()
                            idcode.department="Treasury"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="Treasury").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="FIN-TRE-"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data1['first_name']
                            last_name=data1['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post1.first_name=g
                            post1.last_name=h

                            post.save()
                            post1.save()
                            id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')


                        elif designation =="Compensation And Benefits Processor" or designation=="Employee Relations Processor" or designation=="HR Assistant"or designation=="Human Resource Generalist"or designation=="OIC, Compensation And Benefits Section"or designation=="OIC, Employee Relations Section"or designation=="Records In-Charge"or designation=="Recruitment And Hiring Processor"or designation=="Recruitment And Hiring Section Supervisor"or designation=="Training And Development Section Supervisor"or designation=="Training Associate":
                            idcode=Idcode()
                            idcode.department="Human Resource"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="Human Resource").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="ADM-HRD-"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data1['first_name']
                            last_name=data1['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post1.first_name=g
                            post1.last_name=h

                            post.save()
                            post1.save()
                            id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')



                        elif designation =="Gasman" or designation=="Inventory Management Requisition Analyst" or designation=="Inventory Withdrawal Processor"or designation=="Stock Analyst"or designation=="IMD Reception"or designation=="Inventory Management Withdrawal Analyst (Central/Project)"or designation=="Inventory Variance Report Processor"or designation=="Toolkeeper"or designation=="IMD-Junior Parts Specialist"or designation=="OIC, Inventory Management Section 13"or designation=="Inventory Management Stock Analyst"or designation=="Materials Receiving Processor"or designation=="Inventory Management Withdrawal Analyst (Project)"or designation=="Inventory Management Parts Specialist"or designation=="Lube Stockman"or designation=="Inventory Management Withdrawal Encoder - Central"or designation=="Inventory Management Receiving Analyst"or designation=="Inventory Management Control Specialist"or designation=="Inventory Management Processor"or designation=="Inventory Control Specialist"or designation=="Inventory Management Receiving Analyst (Project)"or designation=="OIC, Inventory Management Section R10"or designation=="Receiving Analyst"or designation=="Warehouse Tender"or designation=="Inventory Management Withdrawal Analyst":
                            idcode=Idcode()
                            idcode.department="IMD"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="IMD").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="ADM-IMD-"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data1['first_name']
                            last_name=data1['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post1.first_name=g
                            post1.last_name=h

                            post.save()
                            post1.save()
                            id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')

                        elif designation =="Bidding And Contracts Officer" or designation =="Bidding And Contracts Processor" or designation =="Contract Handling Processor" or designation =="Marketing Aide" or designation =="Office Engineer" or designation =="OIC, Contracts And Handling Section" or designation =="OIC, Special License Handling Section" or designation =="Special License Compliance Processor":
                            idcode=Idcode()
                            idcode.department="Marketing"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="Marketing").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="MTG-MBD-0"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data1['first_name']
                            last_name=data1['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post1.first_name=g
                            post1.last_name=h

                            post.save()
                            post1.save()
                            id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')


                        elif designation =="Billing Aide" or designation =="Billing Officer" or designation =="Billing Section Supervisor R10" or designation =="Cadd Operator" or designation =="Civil 3D Operator" or designation =="Cost Engineer" or designation =="Monitoring Engineer" or designation =="OIC, Billing Section R13" or designation =="Project Monitoring Section Supervisor" or designation =="Quantity Engineer" or designation =="Technical Assistant" or designation =="Technical Engineer" or designation =="Technical Officer" or designation =="Technical Services Processor":
                            idcode=Idcode()
                            idcode.department="TSD"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="TSD").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="ENG-TSD-0"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data1['first_name']
                            last_name=data1['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post1.first_name=g
                            post1.last_name=h

                            post.save()
                            post1.save()
                            id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')


                        elif designation =="Canvassing Processor"or designation =="Purchaser" or designation =="Procurement Processor" or designation =="Purchasing Processor" or designation =="Records Processor" or designation =="OIC, Canvassing Division R13" or designation =="OIC, Canvassing Section R10" or designation =="PO Processor" or designation =="Procurement Analyst R10" or designation =="Canvassing Proccesor" or designation =="Turn-Over Processor" or designation =="Procurement Analyst R13" or designation =="OIC, Logistics Section R13" or designation =="Canvassing Processor R13" or designation =="Procurement Processor R13":
                            idcode=Idcode()
                            idcode.department="PROCUREMENT"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="PROCUREMENT").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="ADM-LOG-"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data1['first_name']
                            last_name=data1['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post1.first_name=g
                            post1.last_name=h

                            post.save()
                            post1.save()
                            id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')



                        elif designation =="Accounting And Recording Audit Supervisor" or designation =="Document Controller" or designation =="Document Custodian" or designation =="Field Auditor" or designation =="Internal Audit System Assistant" or designation =="Internal Control Financial Reporting Division Head" or designation =="OIC, IAS QMS Section" or designation =="QMS Assistant":
                            idcode=Idcode()
                            idcode.department="IAS"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="IAS").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="IAS-QMS-0"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data1['first_name']
                            last_name=data1['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post1.first_name=g
                            post1.last_name=h

                            post.save()
                            post1.save()
                            id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')


                        elif designation =="Asphalt Heating Operator" or designation =="Assistant Plant Operator"or designation =="Checker"or designation =="Clerical Processor"or designation =="Compliance Section Supervisor"or designation =="Foreman"or designation =="Heating Operator"or designation =="Mining Engineer"or designation =="Plant Account Analyst"or designation =="Plant Aide"or designation =="Plant Electrician"or designation =="Plant Maintenance"or designation =="Plant Operator"or designation =="Plant Processor"or designation =="Plant Supervisor"or designation =="Plant Technician"or designation =="Plants Processor"or designation =="Project Cashier"or designation =="Project Safety Aide"or designation =="Social Development Officer"or designation =="Truckscale Operator":
                            idcode=Idcode()
                            idcode.department="Production"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="Production").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="OPR-PROD-0"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data1['first_name']
                            last_name=data1['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)

                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post1.first_name=g
                            post1.last_name=h

                            post.save()
                            post1.save()
                            id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')



                        elif designation =="Chemical Laboratory Supervisor" or designation =="Chemist" or designation =="Laboratory Aide" or designation =="Laboratory Technician" or designation =="Materials Assistant" or designation =="Materials Engineer" or designation =="Physical Labortory Supervisor" or designation =="Quality Control Engineer":
                            idcode=Idcode()
                            idcode.department="Materials Quality Control"
                            idcode.user_id=request.user.id
                            a=Idcode.objects.filter(department="Materials Quality Control").latest('id_code')
                            b=a.id_code
                            c=b.split("-")
                            d=c[-1]
                            f=int(d)
                            g=f+1
                            h=str(g)
                            code="OPR-QC-0"+h
                            idcode.id_code=code
                            idcode.save()

                            post.id_code=code



                            contact_person_address=data['contact_person_address']
                            midle_initial=data['midle_initial']
                            address=data['address']
                            name_extension=data['name_extension']
                            contact_person=data['contact_person']
                            blood_type=data['blood_type']
                            first_name=data1['first_name']
                            last_name=data1['last_name']


                            a=string.capwords(contact_person_address)
                            b=string.capwords(midle_initial)
                            c=string.capwords(address)
                            d=string.capwords(name_extension)
                            e=string.capwords(contact_person)
                            f=string.capwords(blood_type)
                            g=string.capwords(first_name)
                            h=string.capwords(last_name)



                            post.first_name=g
                            post.last_name=h
                            post.contact_person_address=a
                            post.midle_initial=b
                            post.address=c
                            post.name_extension=d
                            post.contact_person=e
                            post.blood_type=f
                            post1.first_name=g
                            post1.last_name=h

                            post.save()
                            post1.save()
                            id_application.save()
                            messages.success(request,f'Successfully Apply for ID')
                            return redirect('status')

                else:
                    if not DeptandDesignation.objects.filter(fullname=name):

                        contact_person_address=data['contact_person_address']
                        midle_initial=data['midle_initial']
                        address=data['address']
                        name_extension=data['name_extension']
                        contact_person=data['contact_person']
                        blood_type=data['blood_type']
                        first_name=data1['first_name']
                        last_name=data1['last_name']


                        a=string.capwords(contact_person_address)
                        b=string.capwords(midle_initial)
                        c=string.capwords(address)
                        d=string.capwords(name_extension)
                        e=string.capwords(contact_person)
                        f=string.capwords(blood_type)
                        g=string.capwords(first_name)
                        h=string.capwords(last_name)
                        print("walay match")
                        print(name)

                        post.first_name=g
                        post.last_name=h
                        post.contact_person_address=a
                        post.midle_initial=b
                        post.address=c
                        post.name_extension=d
                        post.contact_person=e
                        post.blood_type=f
                        post1.first_name=g
                        post1.last_name=h

                        post.save()
                        post1.save()

                        id_application.save()
                        messages.success(request,f'Successfully Apply for ID SHIT')
                        return redirect('status')

                    else:

                        oldname=DeptandDesignation.objects.filter(fullname=name)
                        for nn in oldname:
                                print(nn.fullname)

                        contact_person_address=data['contact_person_address']
                        midle_initial=data['midle_initial']
                        address=data['address']
                        name_extension=data['name_extension']
                        contact_person=data['contact_person']
                        blood_type=data['blood_type']
                        first_name=data1['first_name']
                        last_name=data1['last_name']


                        a=string.capwords(contact_person_address)
                        b=string.capwords(midle_initial)
                        c=string.capwords(address)
                        d=string.capwords(name_extension)
                        e=string.capwords(contact_person)
                        f=string.capwords(blood_type)
                        g=string.capwords(first_name)
                        h=string.capwords(last_name)

                        post.id_code = nn.idcode
                        post.first_name=g
                        post.last_name=h
                        post.contact_person_address=a
                        post.midle_initial=b
                        post.address=c
                        post.name_extension=d
                        post.contact_person=e
                        post.blood_type=f
                        post1.first_name=g
                        post1.last_name=h

                        post.save()
                        post1.save()


                        id_application.save()
                        messages.success(request,f'Successfully Apply for ID SHIT')
                        return redirect('status')

        else:
            if not Idapplication.objects.filter(user=request.user):
                foridapplication=Idapplication()
                foridapplication.user=request.user
                trans_no='klay45'+str(random.randint(1111111,9999999))
                foridapplication.transaction_no=trans_no
                foridapplication.save()
                
                print("sa elese ni")


                id_application= ID()
                id_application.user = request.user
                id_application.transaction_no=trans_no
                id_application.save()

        
            

            u_form = UserUpdateForm(request.POST,instance=request.user)

            p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.employee)
         
            




    
            if p_form.is_valid() and u_form.is_valid():
                post = p_form.save(commit=False)
                post1 = u_form.save(commit=False)
                data = p_form.cleaned_data
                data1 = u_form.cleaned_data


                first_name=data1['first_name']
                midle_initial=data['midle_initial']
                name_extension=data['name_extension']
                a=string.capwords(midle_initial)
                a1=a[0]
                last_name=data1['last_name']
                name=first_name+" "+a1+"."+" "+last_name+name_extension
                if not DeptandDesignation.objects.filter(fullname=name):
               
                    contact_person_address=data['contact_person_address']
                    midle_initial=data['midle_initial']
                    address=data['address']
                    name_extension=data['name_extension']
                    contact_person=data['contact_person']
                    #blood_type=data['blood_type']
                    first_name=data1['first_name']
                    last_name=data1['last_name']

                    a=string.capwords(contact_person_address)
                    b=string.capwords(midle_initial)
                    c=string.capwords(address)
                    d=string.capwords(name_extension)
                    e=string.capwords(contact_person)
                    #f=string.capwords(blood_type)
                    g=string.capwords(first_name)
                    h=string.capwords(last_name)

                    #post.id_code=nn.idcode
                    post.first_name=g
                    post.last_name=h
                    post.contact_person_address=a
                    post.midle_initial=b
                    post.address=c
                    post.name_extension=d
                    post.contact_person=e
                    #post.blood_type=f
                    post1.first_name=g
                    post1.last_name=h

                    post.save()
                    post1.save()
                
                    messages.success(request,f'Your Account has been Updated')
                    return redirect('status')
                else:
                    oldname=DeptandDesignation.objects.filter(fullname=name)
                    for nn in oldname:
                        print(nn.fullname)



                    contact_person_address=data['contact_person_address']
                    midle_initial=data['midle_initial']
                    address=data['address']
                    name_extension=data['name_extension']
                    contact_person=data['contact_person']
                    #blood_type=data['blood_type']
                    first_name=data1['first_name']
                    last_name=data1['last_name']

                    a=string.capwords(contact_person_address)
                    b=string.capwords(midle_initial)
                    c=string.capwords(address)
                    d=string.capwords(name_extension)
                    e=string.capwords(contact_person)
                    #f=string.capwords(blood_type)
                    g=string.capwords(first_name)
                    h=string.capwords(last_name)

                    post.id_code=nn.idcode
                    post.first_name=g
                    post.last_name=h
                    post.contact_person_address=a
                    post.midle_initial=b
                    post.address=c
                    post.name_extension=d
                    post.contact_person=e
                    #post.blood_type=f
                    post1.first_name=g
                    post1.last_name=h

                    post.save()
                    post1.save()
                
                    messages.success(request,f'Your Account has been Updated')
                    return redirect('status')





    else:







        if not Employee.objects.filter(user=request.user.id):
            #ddd=DeptandDesignation.objects.all().values()
            u_form = UserUpdateForm(instance=request.user)

            p_form = ProfileUpdateForm()
            
        else:
            
            u_form = UserUpdateForm(instance=request.user)

            p_form = ProfileUpdateForm(instance=request.user.employee)
            #d_form = DeptandDesignationForm(instance=ddd)

    context= {
        'u_form':u_form,
        'p_form':p_form,
        #'d_form':d_form

    }

    return render(request,'userupdateform.html',context)
