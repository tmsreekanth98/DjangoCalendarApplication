from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    name=models.CharField(max_length=250)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField()
    description=models.CharField(max_length=1000)
    created=models.DateTimeField(auto_now_add=True)
    is_favorite=models.BooleanField(default=False)

    def __str__(self):
        return self.name + " - "+ str(self.date)
