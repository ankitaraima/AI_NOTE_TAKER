from django.db import models
from django.contrib.auth.hashers import make_password
from noteTakerApp.record import transcribe_audio
# Create your models here.
import datetime
class User(models.Model):
    user_id = models.AutoField(primary_key=True)  # Custom primary key
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, password):
        self.password = make_password(password)

    def check_password(self, password):
        from django.contrib.auth.hashers import check_password
        return check_password(password, self.password)

    def __str__(self):
        return self.name
    
class History(models.Model):
    history_id = models.AutoField(primary_key=True)  # Custom primary key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=255)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    transcribe_audio=models.CharField(max_length=255,default=None)
    transcribe_file=models.CharField(max_length=255,default=None)
 
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.history_id    
    
    