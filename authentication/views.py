from tokenize import group
from unicodedata import name
from django import http
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User, Group
from api.models import District, Profile
from . models import Service
from django.core.mail import send_mail

from authentication.models import Service


# here I create my views which are simply python functions that take in a web request, and then return a web response

# declaring the home page request
def home(request):
    is_superuser = User.objects.filter(groups__name="superuser")
    context = {"is_superuser": is_superuser}
    return render(request, "index.html", context)

def login(request):
    is_superuser = User.objects.filter(groups__name="superuser")
    context = {"is_superuser": is_superuser}
    #if request.method == 'POST':
    #    username = request.POST['username']
    #    pass1 = request.POST['pass1']
    #    user = auth.authenticate(username=username, password=pass1)
    #
    #    if user is not None:
    #        auth.login(request, user)
    #        return redirect('home')
    #    else:
    #        messages.error(request,"Incorrect Credentials!")
    #        return redirect('login')

    return render(request, "authentication/login.html", context)


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')


def caregivers_admin(request):
    is_superuser = User.objects.filter(groups__name="superuser")
    if request.method == 'GET':
        caregivers = User.objects.filter(groups__name='Caregiver')
        context={'caregivers':caregivers, "is_superuser": is_superuser}
        return render(request, "admin/caregivers-admin.html", context)
    else:
        context = {"is_superuser": is_superuser}
        print(request.body)
        return HttpResponse(request.body, context)

def clients_admin(request):
    is_superuser = User.objects.filter(groups__name="superuser")
    if request.method == 'GET':
        clients = User.objects.filter(groups__name='Client')
        services = Service.objects.all()
        context = {'clients':clients, 'services':services, "is_superuser": is_superuser}
        return render(request, "admin/clients-admin.html", context)
    else:
        context = {"is_superuser": is_superuser}
        print(request.body)
        return HttpResponse(request.body, context)


def caregiver_form(request):
    is_superuser = User.objects.filter(groups__name="superuser")
    context = {"is_superuser": is_superuser}
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        district_codes = request.POST.getlist('districtcode')
        dateofbirth = request.POST.get('dateofbirth')
        address = f"{request.POST.get('flatnumber')}, {request.POST.get('building')}, {request.POST.get('street')}, {request.POST.get('city')}, {request.POST.get('postcode')}"
        phone_number = request.POST.get('phonenumber')
        bio = request.POST.get('bio')


        # guard clause
        if pass1 != pass2:
            return HttpResponse("passwords dont match")
        user = User()
        user.username = username
        user.first_name = fname
        user.last_name = lname
        user.email = email
        user.password = pass1
        user.is_active = 0
        user.save()

        caregiver_group = Group.objects.get(name='Caregiver')
        caregiver_group.user_set.add(user)

        profile = Profile.objects.create(user=user, bio='lorem ipsum')
        profile.save()

        for district in district_codes:
            user.profile.service_areas.add(District.objects.get(code=district))

        print(username, fname, lname, email, pass1, pass2, district_codes)
        link = f"{request.build_absolute_uri('/users/approve')}/{user.id}"
        send_mail(
            f'{user.first_name} {user.last_name} has signed up',
            f'''
            Username: {username}
            Name: {user.first_name} {user.last_name}
            Address: {address}
            Email Address: {user.email}
            District Codes: {district_codes}
            Date of Birth: {dateofbirth}
            Phone Number: {phone_number}
            Bio: {bio}


            Click the following link to activate user: 
            {link}''',
            'examplecouncilemail@gmail.com', ['examplecouncilemail@gmail.com'], fail_silently=False
        )

        return redirect('/', context)
    else:
        districts=District.objects.all()
        context={'districts':districts, "is_superuser": is_superuser}
        return render(request, 'authentication/caregiver_form.html', context)


def clients_admin_form(request):
    is_superuser = User.objects.filter(groups__name="superuser")
    context = {"is_superuser": is_superuser}
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        services = request.POST.get('services')

        user = User()
        user.username = username
        user.first_name = fname
        user.last_name = lname
        user.email = email
        user.password = pass1
        user.is_active = 1
        user.save()

        client_group = Group.objects.get(name='Client')
        client_group.user_set.add(user)

        profile = Profile.objects.create(user=user)
        profile.save()

        for service in services:
            user.profile.services.add(Service.objects.get(name=service))

        return redirect('/', context)
    else:
        services=Service.objects.all()
        context={'services':services, "is_superuser": is_superuser}
        return render(request, 'admin/clients-admin.html', context)

    
def activateUser(request, id):
    user = User.objects.get(id=id)
    user.is_active = 1
    user.save()
    return HttpResponse('<h1>User activated</h1>')






  #  class handleCaregiver:
  #      def __init__(self, username, fname, lname, districtcode, dateofbirth) -> any:
  #          self.username = username
 #          self.first_name = fname
 #           self.last_name = lname
  #          self.email_address = email
 #           self.district_code = districtcode
  #          self.date_of_birth = dateofbirth
  #          self.is_active = False

        # handleCaregiver variable declared
  #      handleCaregiver = handleCaregiver(username, fname, lname, districtcode, dateofbirth)

        # success message 
  #      messages.success = (request, "Success! You have submitted your request to become a perspective caregiver! It will be reviewed and you will be update on the outcome")


    
        
    # send email with perspective caregiver's details to be reviewed