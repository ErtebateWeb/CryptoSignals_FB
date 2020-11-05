from django import forms
from django.forms import ModelForm
from .models import signal

class submitsignalForm(forms.Form):
    SymbolTitle = forms.CharField(max_length=40, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter SymbolTitle', 'aria-label' : 'SymbolTitle', 'aria-describedby' : 'add-btn'}))
    TimeFrame = forms.CharField(max_length=40, 
            widget=forms.TextInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Enter TimeFrame', 'aria-label' : 'TimeFrame', 'aria-describedby' : 'add-btn'}))
    NowPrice = forms.CharField(max_length=40, 
            widget=forms.TextInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Enter NowPrice', 'aria-label' : 'NowPrice', 'aria-describedby' : 'add-btn'}))
    TriggerPrice = forms.CharField(max_length=40, 
            widget=forms.TextInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Enter TriggerPrice', 'aria-label' : 'TriggerPrice', 'aria-describedby' : 'add-btn'}))
    StopLoss = forms.CharField(max_length=40, 
            widget=forms.TextInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Enter StopLoss', 'aria-label' : 'StopLoss', 'aria-describedby' : 'add-btn'}))
    TakeProfit1 = forms.CharField(max_length=40, 
            widget=forms.TextInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Enter TakeProfit1', 'aria-label' : 'TakeProfit1', 'aria-describedby' : 'add-btn'}))
    TakeProfit2 = forms.CharField(max_length=40, 
                widget=forms.TextInput(
                    attrs={'class' : 'form-control', 'placeholder' : 'Enter TakeProfit2', 'aria-label' : 'TakeProfit2', 'aria-describedby' : 'add-btn'}))
    TakeProfit3 = forms.CharField(max_length=40, 
                widget=forms.TextInput(
                    attrs={'class' : 'form-control', 'placeholder' : 'Enter TakeProfit3', 'aria-label' : 'TakeProfit3', 'aria-describedby' : 'add-btn'}))
    TakeProfit4 = forms.CharField(max_length=40, 
                widget=forms.TextInput(
                    attrs={'class' : 'form-control', 'placeholder' : 'Enter TakeProfit4', 'aria-label' : 'TakeProfit4', 'aria-describedby' : 'add-btn'}))


class SignalModelForm(ModelForm):
    class Meta:
        model = signal
        # fields = '__all__'
        fields =['SymbolTitle','TimeFrame','NowPrice','TriggerPrice','StopLoss','TakeProfit1','TakeProfit2','TakeProfit3','TakeProfit4',]