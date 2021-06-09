from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator

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

    @classmethod
    def get_categories(cls):
        categories = Category.objects.all()
        return categories

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Product(models.Model):
    name= models.CharField(max_length=300)
    image= CloudinaryField('image',null=True)
    description= models.TextField()
    Specifications = models.TextField(null=True)
    Brand = models.CharField(max_length=50,null=True)
    price = models.PositiveIntegerField()
    image1= CloudinaryField('image',null=True, blank=True)
    image2= CloudinaryField('image',null=True, blank=True)
    image3= CloudinaryField('image',null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='')
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

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

    @classmethod
    def filter_by_category(cls, category):
        product = Product.objects.filter(category__name=category).all()
        return product

    @classmethod
    def search_product(cls, name):
        return cls.objects.filter(name__icontains=name).all()


class Feedback(models.Model):
    title = models.CharField(max_length=100, null=True)
    feedback = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='feedback_owner')
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='product_feedback')

    class Meta:
       ordering = ['-date']

    def __str__(self):
        return self.title


class SubscriptionRecipients(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()


class Cart(models.Model):
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)

    @classmethod
    def in_cart(cls, product, user):
        return Cart.objects.filter(product=product, user=user, purchased=False).exists()

    @classmethod
    def get_user_cart(cls, user):
        return Cart.objects.filter(user=user).all()

    @classmethod
    def add_product(cls, product, user):
        if not Cart.objects.filter(product=product, user=user, purchased=False).exists():
            Cart.objects.create(product=product, user=user)

    @classmethod
    def remove_product(cls, product, user):
        if Cart.objects.filter(product=product, user=user, purchased=False).exists():
            Cart.objects.filter(product=product, user=user).delete()


class Payment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100, null=True)
    card_number = models.IntegerField()

    
