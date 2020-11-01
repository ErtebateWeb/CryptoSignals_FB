from django.shortcuts import render
from django.http import HttpResponse
from .models import signal
 
# Create your views here.

def home(request):
    qs = signal.objects.all()
    context = {
        "objects": qs
    }
    print(context)
    return render(request, "signals/signal_list.html", context)