from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    fullname = models.CharField(max_length=50, null=False, unique=True)
    born_date = models.DateField(auto_now_add=False)
    born_location = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=20000, null=False)

    def __str__(self):
        return f"{self.fullname}"

class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"

class Quote(models.Model):
    quote = models.CharField(max_length=2000, null=False)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  

    def __str__(self):
        return f"{self.quote}"