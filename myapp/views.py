from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm
from django.contrib import messages

from django.contrib.auth import authenticate,logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login as login_user

from myapp.models import patient
from myapp.models import Data
from myapp.models import DocProfile
from myapp.models import DocProfile
from django.db.models import Q
from myapp.models import Payment,Feedback
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def home(request):
    return render(request,"home.html")


def index(request):
    if 'q' in request.GET:
        q=request.GET['q']
        #data=Data.objects.filter(first_name__icontains=q)
        multiple_q=Q(Q(name__icontains=q) | Q(email__icontains=q) | Q(op__icontains=q) )
        data=Payment.objects.filter(multiple_q)

    else:
        data=Payment.objects.all()

    context={
        'data':data
    }
    return render(request,'reminder.html',context)


def register(request):
    if request.user.is_authenticated:
        return redirect('Pboard')
    else:

        form=CreateUserForm()

        

           
 
    
        form=CreateUserForm(request.POST)
        if form.is_valid():
               form.save()

               user=form.cleaned_data.get('username')

               messages.success(request,'Account has created for ' + user)
            
               return redirect('login')

        if request.method=="POST":
            username=request.POST.get('username')
            email=request.POST.get('email')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            Patient=patient(username=username,email=email,password1=password1,password2=password2)

            Patient.save()

            


        context={'form':form}
        return render(request,"register.html",context)

   


def loginP(request):
    if request.user.is_authenticated:
        return redirect('Pboard')
    else:
        if request.method=="POST":
            
           username=request.POST.get('username')
           password=request.POST.get('password')

           user=authenticate(request,username=username,password=password)

           if user is not None:
               login_user(request,user)
               return redirect('myapp')

           else:
               messages.info(request,"Username or Password is incorrect")
            

        context={}
        return render(request,"login.html",context)

    

def logoutU(request):
    logout(request)
    return redirect('myapp')


    


def doctorSignUp(request):
    if request.user.is_authenticated:
        return redirect('Dboard')
    else:

        form=CreateUserForm()

        if request.method=="POST":
 
    
           form=CreateUserForm(request.POST)
           if form.is_valid():
               form.save()

               user=form.cleaned_data.get('username')

               messages.success(request,'Account has created for ' + user)
            
               return redirect('doctorLogin')

        context={'form':form}
        return render(request,"doctorSignUp.html",context)
def mail(request):
    return render(request,"mail.html")


def loginD(request):
    
    if request.user.is_authenticated:
        return redirect('Dboard')
    else:
        if request.method=="POST":
            
           username=request.POST.get('username')
           password=request.POST.get('password')

           user=authenticate(request,username=username,password=password)

           if user is not None:
               login_user(request,user)
               return redirect('Dboard')

           else:
               messages.info(request,"Username or Password is incorrect")
            

        context={}
        return render(request,"doctorLogin.html",context)




def doctorProfile(request):

    if request.method == "POST":
        name=request.POST["name"]
        
        email=request.POST["email"]
        degree=request.POST["degree"]
        op=request.POST["op"]
        institute=request.POST["institute"]
        specialist=request.POST["specialist"]
        fees=request.POST["fees"]

        doctor_profile=DocProfile(name=name,email=email,degree=degree,op=op,institute=institute,specialist=specialist,fees=fees)

        doctor_profile.save()
    return render(request,"doctorProfile.html")


def bio(request):


    docData=DocProfile.objects.all()
    # for a in docData:
    #     print(a.name)
    # print(docData)
    if 'q' in request.GET:
        q=request.GET['q']
        #data=Data.objects.filter(first_name__icontains=q)
        multiple_q=Q(Q(name__icontains=q) | Q(fees__icontains=q) | Q(specialist__icontains=q) |Q (op__icontains=q))
        docData=DocProfile.objects.filter(multiple_q)

    else:
        docData=DocProfile.objects.all()

    data={
        "docData":docData
    }


    return render(request,"bio.html",data)



def payment(request):
    
    if request.method == "POST":
        name=request.POST["name"]
        email=request.POST["email"]
        op=request.POST["op"]
        card=request.POST["card"]

        pay=Payment(name=name,email=email,op=op,card=card)

        pay.save()

        return redirect("success")

    
        
    return render(request,"payment.html")

# def reminder(request):
#     if 'q' in request.GET:
#         q=request.GET['q']
#         #data=Data.objects.filter(first_name__icontains=q)
#         multiple_q=Q(Q(name__icontains=q) | Q(email__icontains=q) |Q(op__icontains=q))
#         data=Data.objects.filter(multiple_q)

#     else:
#         data=Payment.objects.all()

#     context={
#         'data':data
#     }
#     return render(request,'index.html',context)



def success(request):
    return render(request,"success.html")

@login_required(login_url="login")
def Pboard(request):
    return render(request,"patientDashboard.html")

@login_required(login_url="doctorLogin")
def Dboard(request):
    return render(request,"doctorDashboard.html")


def feedback(request):
    if request.method == "POST":
        name=request.POST["name"]
       
        exp=request.POST["exp"]

        feed=Feedback(name=name,exp=exp)

        feed.save()

        
    return render(request,"feedback.html")



def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        
        return HttpResponse('Make sure all fields are entered and valid.')
