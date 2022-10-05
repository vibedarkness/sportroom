
from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from matplotlib.pyplot import cla
# Create your models here.


class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Gerant"),(3,"Client"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Gerant(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    telephone=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    def __str__(self):
        return self.admin.last_name + " " + self.admin.first_name

class Client(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    age=models.IntegerField()
    telephone=models.CharField(max_length=50)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.admin.last_name + " " + self.admin.first_name

class Calendrier(models.Model):
    date=models.DateField()
    heure_debut=models.TimeField()
    heure_fin=models.TimeField()

class Reservation(models.Model):
    gerant=models.ForeignKey(Gerant, on_delete=models.CASCADE)
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    calendrier=models.ForeignKey(Calendrier, on_delete=models.CASCADE)

class Terrain(models.Model):
    gerant=models.ForeignKey(Gerant, on_delete=models.CASCADE)
    reservation=models.ForeignKey(Reservation, on_delete=models.CASCADE)
    nom=models.CharField(max_length=100)
    adresse=models.CharField(max_length=300)
    image=models.ImageField()
    surface=models.IntegerField()
    description=models.TextField()
    longitude=models.DecimalField(max_digits=9, decimal_places=6) 
    latitude=models.DecimalField(max_digits=9, decimal_places=6) 

class Localite(models.Model):
    nom = models.CharField(max_length=100)
    terrain=models.ForeignKey(Terrain, on_delete=models.CASCADE)

class Publication(models.Model):
    gerant=models.ForeignKey(Gerant, on_delete=models.CASCADE)
    description=models.TextField()
    date_publication=models.DateTimeField()

class NotificationGerant(models.Model):
    gerant = models.ForeignKey(Gerant, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

















@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Gerant.objects.create(admin=instance,address="",telephone="")
        if instance.user_type==3:
            Client.objects.create(admin=instance,address="",telephone="",age="")

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.gerant.save()
    if instance.user_type==3:
        instance.client.save()