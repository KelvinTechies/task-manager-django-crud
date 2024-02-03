from django.db import models

# Create your models here.


class Record(models.Model):
    creation_date=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)
    task=models.CharField(max_length=300)
    description=models.CharField(max_length=300)


    def __str__(self):
        return self.first_name+ " " + self.last_name