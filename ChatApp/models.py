from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    from_who = models.ForeignKey(User,on_delete=models.PROTECT,default=None,related_name = 'from_who')
    to_who = models.ForeignKey(User,on_delete=models.PROTECT,default=None,related_name = 'to_who')
    message = models.TextField()
    date = models.DateField(null = True)
    time = models.TimeField(null = True)
    has_been_seen = models.BooleanField(null = True,default = False)
    def __str__(self):
        return (f'{self.from_who}->{self.to_who}  {self.message}')
    
class UserChannel(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT,default=None)
    channel_name = models.TextField()