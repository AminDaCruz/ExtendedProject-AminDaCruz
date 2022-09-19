from authentication.models import Service
from django.db import models
from django.contrib.auth.models import User

# declaring the Users class 
# this model will store the user's information
#class Users(models.Model):
#    username = models.CharField(max_length=10)
#    fname = models.CharField(max_length=15)
#    lname = models.CharField(max_length=15)
#    email = models.EmailField()
#    pass1 = models.CharField(max_length=15)
#    districtcode = models.CharField(max_length=4)
#    dateofbirth = models.DateField()

# declaring the caregivers class
# this model will store the caregiver's information which will be inputted directly into the database at the council

#class Caregivers(models.Model):
#    id = models.AutoField(primary_key=True)
#    username = models.CharField(max_length=10)
#    fname = models.CharField(max_length=15)
#    lname = models.CharField(max_length=15)
#    email = models.EmailField()
#    pass1 = models.CharField(max_length=15)
#    districtcode = models.CharField(max_length=4)
#    dateofbirth = models.DateField()

#class Caregiver(User):
#    pass

#class Client(User):
#    pass




#class Caregiver(models.Model):
#    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

#class Client(models.Model):
#    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

class District(models.Model):
    code = models.CharField(max_length=4)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    district_code = models.CharField(max_length=8, null=True, blank=True)
    service_areas = models.ManyToManyField(District)
    services = models.ManyToManyField(Service)
    
    def __str__(self):
        return str(self.user)
