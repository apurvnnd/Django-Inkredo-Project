from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=256)
    ceo = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("inkredoapp:detail",kwargs={'pk':self.pk})


class User(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    company = models.ForeignKey(Company,related_name='users')

    def __str__(self):
        return self.name
