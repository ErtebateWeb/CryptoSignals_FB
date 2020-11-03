from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import signal
from .forms import submitsignalForm
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User


 
# Create your views here.
# def index(request):
#     signal_list = signal.objects.all().filter(IsActive=True).order_by('-id')
#     context ={'signal_list': signal_list}
#     return render(request,'signals/index.html',context)




def home(request):
    qs = signal.objects.all()
    context = {
        "objects": qs
    }
    print(context)
    return render(request, "signals/signal_list.html", context)



def submit_signal(request):
    # if request.method == 'POST':
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('signals/signal_list.html')
    # else:
    #     form = PostForm()
    # return render(request, 'submit_signal.html', {'form': form})
    signal_list = signal.objects.all().filter(IsActive=True).order_by('-id')
    form = submitsignalForm()
    context ={'signal_list': signal_list,'frm': form}
    
    
    return render(request,'signals/index.html',context)

@require_POST
def addsignal(request):
    form = submitsignalForm(request.POST)
    # print('user =',request.user)
    if form.is_valid():
        newsignal = signal(SymbolTitle = request.POST['SymbolTitle'],NowPrice ='10' ,TriggerPrice='12',StopLoss='9',TakeProfit1='15',created_by=request.user )
        newsignal.save()

    # print(request.POST['SymbolTitle'])
    # print(newsignal)
    return redirect('submit')



