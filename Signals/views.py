from django.shortcuts import render
from django.http import HttpResponse
from .models import signal
 
# Create your views here.

def home(request):
    qs = signal.objects.all()
    Signals_title = list()
    for s in qs:
        Signals_title.append(s.SymbolTitle)
    response_html = '<br>'.join(Signals_title)
    return HttpResponse(response_html)