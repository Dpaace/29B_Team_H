from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AddBook(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset()
        
    book_id = models.AutoField(auto_created=True, primary_key=True)
    b_name = models.CharField(max_length=100, blank=True)
    b_desc = models.CharField(max_length=250, blank=True)
    auther=models.CharField(max_length=100, blank=True)
    b_genre=models.CharField(max_length=100, blank=True)
    b_price=models.IntegerField(blank=True)
    b_pic= models.FileField(upload_to='books', blank=True)
    slug=models.SlugField(max_length=120, blank=True)
    favourite =models.ManyToManyField(User, related_name='favourite', blank=True)
    objects=models.Manager() #default manager
    newmanager= NewManager() #custom manager
    class Meta:
        db_table="addbook"