from django.db import models

# Create your models here.
class Book(models.Model):
    title= models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    langauge=models.CharField(max_length=100)
    edition=models.TextField(max_length=50)
    description=models.TextField()
    image=models.ImageField(upload_to='book/images/')


    def __str__(self):
        return self.title
        
class Review(models.Model):
    book=models.ForeignKey( Book, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    ratings=models.IntegerField()
    review=models.TextField()

    def __str__(self):
        return f'{self.book},{self.name}'

    
