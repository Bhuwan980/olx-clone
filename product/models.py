from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

CHOICES = (('new','NEW'),('used','USED'))
class Product(models.Model):
    name = models.CharField(max_length=40)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True,blank=True)
    brand = models.ForeignKey('Brands',on_delete=models.SET_NULL,null=True,blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='product_image/',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    condition = models.TextField(choices=CHOICES)
    price = models.DecimalField(max_digits=15,decimal_places=2)

    slug = models.SlugField(null=True,blank=True)

    def save(self,*arg,**karg):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Product,self).save(*arg,**karg) 


    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(max_length=20,null=True,blank=True)
    image = models.ImageField(upload_to='category_image/')
    
    def __str__(self):
        return self.category

class Brands(models.Model):
    brand = models.CharField(max_length=20,null=True,blank=True)
   
    def __str__(self):
        return self.brand
