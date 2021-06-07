from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #name = models.CharField(blank=True, max_length=120)
    profile_picture = CloudinaryField('image',null=True, default='default.png')
    location = models.CharField(max_length=100, blank=True)
    phone_number = models.IntegerField(null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'{self.user.username} Profile'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Product(models.Model):
    name= models.CharField(max_length=300)
    image= CloudinaryField('image',null=True)
    description= models.TextField()
    price = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='')

    class Meta:
       ordering = ['-date']
    
    def __str__(self):
        return self.name

    @classmethod
    def all_products(cls):
        return cls.objects.all()

    def save_product(self):
        self.save()

    def delete_product(self):
        self.delete()


    
