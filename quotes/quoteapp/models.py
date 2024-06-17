from django.db import models


# Create your models here.
class Author(models.Model):
    fullname = models.CharField(max_length=25, null=False, unique=True)
    born_date = models.DateTimeField(auto_now_add=False)
    born_location = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=1500, null=False)

    def __str__(self):
        return f"{self.fullname}"


class Quote(models.Model):
    quote = models.CharField(max_length=500, null=False)
    tags = models.CharField(max_length=500, null=False)
    author = models.ManyToOneRel(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
