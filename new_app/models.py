from django.db import models
from django.contrib.auth.models import User

class All_Xarajat(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description_xarjat = models.TextField()
    miqdori = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name