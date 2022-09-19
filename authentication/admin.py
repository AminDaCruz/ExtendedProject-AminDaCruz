from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Service

#from .models import CustomUser

admin.site.register(Service)