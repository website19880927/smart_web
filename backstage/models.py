from django.db import models

# Create your models here.
class User(models.Model):
    #定义用户类
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    class Meta:
        db_table = 't_user'



