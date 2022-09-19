from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.core import serializers
from django.views.generic import DetailView
from api.models import Profile
from .forms import EditProfileForm 
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt



#data = serializers.serialize("python", User.objects.all())
#context = {
#   'data':data
#}

#group = Group.objects.get(name='caregiver')

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    success_message = 'You have successfully updated your password!!'


class UserEditView(generic.UpdateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_superuser'] = User.objects.filter(groups__name="superuser")
        return context
    form_class = EditProfileForm
    template_name = 'registration/edit_account.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

def jobs(request):
    is_superuser = User.objects.filter(groups__name="superuser")
    if request.method == 'GET':
        caregivers = User.objects.filter(groups__name='Caregiver')
        caregivers_in_users_district_code = []
        for caregiver in caregivers:
            if caregiver.profile.service_areas.filter(code=request.user.profile.district_code).exists():
                caregivers_in_users_district_code.append(caregiver)
        context={'caregivers':caregivers_in_users_district_code, "is_superuser": is_superuser}
        return render(request, "menu/jobs.html", context)
    else:
        context = {"is_superuser": is_superuser}
        print(request.body)
        return HttpResponse(request.body, context)


def about(request):
    is_superuser = User.objects.filter(groups__name="superuser")
    context = {"is_superuser": is_superuser}
    return render(request, "menu/about.html", context)



#def base(request):
#    user_id = request.user.id
#    is_client =  user_id in [user.id for user in User.objects.filter(group__name='client')]
#    context = {'is_client':is_client}
#    return(context)