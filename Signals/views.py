from django.shortcuts import render
from django.http import HttpResponse
from .models import signal
 
# Create your views here.

def home(request):
    qs = signal.objects.all()
    Signals_title = list()
    for s in qs:
        Signals_title.append("symbol:{}--Now Price:{}--Active:{}--created_at:{}--created_by{}".format(s.SymbolTitle,s.NowPrice,s.IsActive,s.created_at,s.created_by))
    
    response_html = Signals_title
    
    return HttpResponse(response_html)