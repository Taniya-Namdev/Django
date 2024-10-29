from django.db import models
from django.utils import timezone

# Create your models here.
class BookVariety(models.Model):
    book_type_choice = [('FI','Fictional'),('RM','Romance'),('HR','Horror'),('CD','Comedy')]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Books/')
    date_added = models.DateTimeField(default = timezone.now)
    type = models.CharField(max_length=2,choices =(book_type_choice))
    def __str__(self) :
        return self.name()                                                     
    
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
