from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
     firstname = models.CharField(max_length=255)
     lastname = models.CharField(max_length=255)
     email = models.CharField(max_length=255)
     phone = models.IntegerField(null=True)
     created_at =models.DateTimeField(auto_now_add=True)

     def __str__(self):
       return self.firstname


class Book(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    title=models.CharField(max_length=225)
    publisher=models.CharField(max_length=225)
    synopsis=models.CharField(max_length=750)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['created_at']

    def __str__(self):
       return self.title
        