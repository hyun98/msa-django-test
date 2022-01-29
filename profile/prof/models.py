from django.db import models
import datetime

# Create your models here.

class Profile(models.Model):
    user_id = models.IntegerField(unique=True)
    last_login = models.DateTimeField("마지막 로그인", null=True)
    
    class Meta:
        db_table = "profile"
        
    # @last_login.setter
    # def last_login(self, val):
    #     self.last_login = datetime.datetime.strptime(val)