from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import auth

from proselloapp.forms import UserRegisterForm

from properties.models import Property
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from properties.forms import PropertyForm
from django.contrib.auth.models import User

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
                form = auth_login(request,user)
                print('user is owner')
                return redirect('ownerhome')
            else:
                form = auth_login(request,user)
                messages.success(request,f'welcome {username} !!')
                return redirect('userhome')
        else:
            messages.info(request,'invalid username and password')

    form = AuthenticationForm()
    return render (request,'login.html')

@login_required()
def ownerhome(request):
    print("enetred ownerhome")
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
        print("opened property form")

        if form.is_valid():
            print("property form is valid")

            thought = form.save(commit=False)
            thought.user = request.user
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

@login_required()
def view_property_owner(request):
    property_list = Property.objects.all()
    print("Output", property_list)
    return render (request, 'view_property_owner.html',{'prop': property_list})




 #delete a property
@login_required()
def delete_property_owner(request, id):
    prop = Property.objects.get(pk = id)
    prop.delete()
    return redirect('view_property_owner')
    # return render (request, 'delete_property.html')


@login_required()
def update_property(request, id):
    property = Property.objects.get(pk=id)
    form = PropertyForm(request.POST or None, instance = property)
    if form.is_valid():
        form.save()
        return redirect('my_property')
    return render (request, 'update_property.html',
    {'prop': property,
    'form':form})
    

@login_required()
def my_property(request):

    property_list = Property.objects.filter(user=request.user)
    print("Output", property_list)
    return render (request, 'my_property.html',{'prop': property_list})


@login_required()
def logout(request):
    auth.logout(request)
    return redirect('index')

@login_required()
def delete_property(request, id):
    property = Property.objects.get(pk=id)
    property.delete()
    # messages.success(request, 'record removed')
    return redirect('my_property')
 