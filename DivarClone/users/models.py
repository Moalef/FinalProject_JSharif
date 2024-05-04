from datetime import timedelta
from django.utils import timezone
import random
import string
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from .senders import send_otp

# Create your models here.
class User(AbstractUser):
    pass

class OtpRequestQuerySet(models.QuerySet):
    def is_valid(self,receiver,request,password):
        current_time = timezone.now()
        return self.filter(
            receiver = receiver,
            request_id = request,
            password = password,
            created__lt = current_time,
            created__gt = current_time - timedelta(seconds=1200000),
        ).exists()

class OTPManager(models.Manager):
    
    def get_queryset(self):
        return OtpRequestQuerySet(self.model , self._db)
    
    def is_valid(self,receiver,request,password):
        return self.get_queryset().is_valid(receiver,request,password)
       
    
    def generate(self,data):
        otp = self.model(channel = data['channel'] , receiver = data['receiver'])
        otp.save(using = self._db)
        send_otp(otp)
        return otp

def generateOTP():
    rand = random.SystemRandom()
    digit = rand.choices(string.digits , k=4)
    return ''.join(digit)


class OTPRequest(models.Model):
    class OtpChannel(models.TextChoices):
        PHONE = 'phone'
        EMAIL = 'E-mail'
    request_id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4())
    channel = models.CharField(max_length=10 , choices=OtpChannel.choices, default=OtpChannel.PHONE)
    receiver = models.CharField( max_length=50)
    password = models.CharField( max_length=4, default=generateOTP)
    created = models.DateTimeField(auto_now_add=True,editable=False)

    objects = OTPManager()
    