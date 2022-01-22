from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

from proselloapp.forms import UserRegisterForm

from properties.models import Property
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from properties.forms import PropertyForm

from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render (request,'index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'Account is created')
                return redirect('index')
            except:
                pass

    else:
        form = UserRegisterForm()
    return render (request,'register.html',{'form':form})


def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password = password)
        if user is not None:
            if user.is_staff == True:
                return redirect('ownerhome')
            else:
                form = auth_login(request,user)
                messages.success(request,f'welcome {username} !!')
                return redirect('userhome') 
        else:
            messages.info(request,'account done not exit plz sign in')
            
    form = AuthenticationForm()  
    return render (request,'login.html')

@login_required()
def ownerhome(request):
    return render (request,'ownerhome.html')

@login_required()
def userhome(request):
    return render (request,'userhome.html')

@login_required()
def add_property(request):
    # f=request.User
    # args = {}
    if request.method == "POST":
        form = PropertyForm(request.POST or None)   
        print("opened property form", form)

        if form.is_valid():
            print("property form is valid")
            
            # thought = form.save(commit=False)
            # thought.User = request.User
            # thought.save()
            # thought.owner = request.user
            form.save()
            messages.success(request, "Property Added")
            return redirect("userhome")
        else:
            print("Error in adding property")
            return render(request, "add_property.html", context={'form': form})
    form = PropertyForm
    return render(request, 'add_property.html', context={'form': form})

@login_required()
def view_property(request):
    property_list = Property.objects.all()
    print("Output", property_list)
    return render (request, 'view_property.html',{'prop': property_list})
 
 
 
 #delete a property   
@login_required()
def delete_property(request, id):
    prop = Property.objects.get(pk = id)
    prop.delete()
    return HttpResponse('deleted')
    

    # return render (request, 'delete_property.html')

@login_required()
def update_property(request, id):
   prop1 = Property.objects.get(pk = id)
   #you can do this for as many fields as you like
   #here I asume you had a form with input like <input type="text" name="name"/>
   #so it's basically like that for all form fields
   prop1.property_name = request.POST.get('name')
   prop1.save()
   return HttpResponse('updated')

@login_required()
def my_property(request):
    # f=request.User
    # property_list2 = Property.objects.filter(User = f)
    # print("Output", property_list2)
    property_list = Property.objects.all()
    print("Output", property_list)
    return render (request, 'view_property.html',{'prop': property_list})
    # return render (request, 'my_property.html',{'prop': property_list2})

#     def delete(request, id):
#    emp = Employee.objects.get(pk = id)
#    emp.delete()
#    return HttpResponse('deleted')

def logout(request):
    logout(request)
    return redirect('index')