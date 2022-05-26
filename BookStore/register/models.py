from django.db import models

# Create your models here.
class AddBook(models.Model):
    book_id = models.AutoField(auto_created=True, primary_key=True)
    b_name = models.CharField(max_length=100, blank=True)
    b_desc = models.CharField(max_length=250, blank=True)
    auther=models.CharField(max_length=100, blank=True)
    b_genre=models.CharField(max_length=100, blank=True)
    b_price=models.IntegerField(blank=True)
    b_pic= models.FileField(upload_to='books', blank=True)

    class Meta:
        db_table="addbook"