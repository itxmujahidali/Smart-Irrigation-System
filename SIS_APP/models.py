from django.db import models

# Create your models here.
class WebUser(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)

    def __str__(self):
        return self.name