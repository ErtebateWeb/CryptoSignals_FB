from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class signal(models.Model):


    SymbolTitle = models.CharField(max_length=30)
    TimeFrame = models.CharField(max_length=30, default='1D')
    NowPrice = models.CharField(max_length=30)
    TriggerPrice = models.CharField(max_length=30)
    StopLoss = models.CharField(max_length=30)
    TakeProfit1 = models.CharField(max_length=30)
    TakeProfit2 = models.CharField(max_length=30, default='',null=True,blank=True)
    TakeProfit3 = models.CharField(max_length=30, default='',null=True,blank=True)
    TakeProfit4 = models.CharField(max_length=30, default='',null=True,blank=True)
    LivePrice = models.CharField(max_length=30, default='',null=True,blank=True)
    
    IsActive = models.BooleanField(default=True)
    IsStopped = models.BooleanField(default=False)
    IsTriggered = models.BooleanField(default=False)
    IsTakeProfited1 = models.BooleanField(default=False)
    IsTakeProfited2 = models.BooleanField(default=False)
    IsTakeProfited3 = models.BooleanField(default=False)
    IsTakeProfited4 = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True,blank=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='signals')
    updated_by = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE, related_name='+')

    Images = models.ImageField(default='', upload_to='images/', null=True,blank=True)
    TelegramMessageId = models.CharField(max_length=30, default='',null=True,blank=True)


    def __str__(self):
            return str(self.SymbolTitle)
