from django.http import HttpResponse
from datetime import datetime
from .models import signal
from .forms import submitsignalForm, SignalModelForm
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, get_object_or_404, redirect

User = get_user_model()

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
    form = SignalModelForm()
    # form = submitsignalForm()
    context ={'signal_list': signal_list,'frm': form}
    
    
    return render(request,'signals/index.html',context)

@require_POST
def addsignal(request):
    form = SignalModelForm()
    # print('user =',request.user)
    print('form is valid=',form.is_valid)
    if request.method=='POST':
        form = SignalModelForm(request.POST)

        if form.is_valid():
            print('form is valid=',form.is_valid)
            print(form.cleaned_data)
            newsignal = signal(SymbolTitle = form.cleaned_data['SymbolTitle'],NowPrice =form.cleaned_data['NowPrice'] ,TriggerPrice=form.cleaned_data['TriggerPrice'],StopLoss=form.cleaned_data['StopLoss'],TakeProfit1=form.cleaned_data['TakeProfit1'],TakeProfit2=form.cleaned_data['TakeProfit2'],TakeProfit3=form.cleaned_data['TakeProfit3'],TakeProfit4=form.cleaned_data['TakeProfit4'],created_by=request.user )
            newsignal.save()
            newsignal.TelegramMessageId='5555'
            newsignal.save()

            # form.save()
            return redirect("/submit")



    # print(newsignal.id)
    # print(newsignal.pk)
    # sig=signal.objects.get(pk=newsignal.pk)
    # sig.TelegramMessageId='9999'
    # print(sig.TelegramMessageId)
    # sig.save()


    # print(request.POST['SymbolTitle'])
    # print(newsignal)
    return redirect('submit')

# @require_POST
def deactivesignal(request,pk):
    sig= signal.objects.get(pk=pk)
    sig.IsActive = False
    sig.save()
    # form = submitsignalForm(request.POST)
    # print('user =',request.user)
    # if form.is_valid():
    #     newsignal = signal(SymbolTitle = form.cleaned_data['SymbolTitle'],NowPrice =form.cleaned_data['NowPrice'] ,TriggerPrice=form.cleaned_data['TriggerPrice'],StopLoss=form.cleaned_data['StopLoss'],TakeProfit1=form.cleaned_data['TakeProfit1'],TakeProfit2=form.cleaned_data['TakeProfit2'],TakeProfit3=form.cleaned_data['TakeProfit3'],TakeProfit4=form.cleaned_data['TakeProfit4'],created_by=request.user )
    #     newsignal.save()
    #     newsignal.TelegramMessageId='5555'
    #     newsignal.save()
    return redirect('submit')


def updatesignal(request,pk):
    print('updatesignal is runnig')
    sig= signal.objects.get(pk=pk)
    print('sig=',sig.created_by)
    form = SignalModelForm(instance=sig)



    # if request.method == 'GET':
    #     print('request.get')
    # # print(form)
    if request.method == 'POST':
         form = SignalModelForm(request.POST or None,instance=sig)
        #  print('request.post')
        
         if form.is_valid():
            print('form is valid:update')
            # print(form.cleaned_data['SymbolTitle'])
            # form = signal(SymbolTitle = form.cleaned_data['SymbolTitle'],NowPrice =form.cleaned_data['NowPrice'] ,TriggerPrice=form.cleaned_data['TriggerPrice'],StopLoss=form.cleaned_data['StopLoss'],TakeProfit1=form.cleaned_data['TakeProfit1'],TakeProfit2=form.cleaned_data['TakeProfit2'],TakeProfit3=form.cleaned_data['TakeProfit3'],TakeProfit4=form.cleaned_data['TakeProfit4'],created_by=request.user )
            form.save()
            
            sig.TelegramMessageId='0000'
            sig.updated_by=request.user
            sig.updated_at= datetime.now()
            sig.save()
            return redirect("/submit")
         else:
            print('Error')  
            return redirect('submit')

    # print(form)
    # print('user =',request.user)
    # print('USer =',User.objects.get(pk=2))
  

    # 


    # print(newsignal.id)
    # print(newsignal.pk)
    # sig=signal.objects.get(pk=newsignal.pk)
    # sig.TelegramMessageId='9999'
    # print(sig.TelegramMessageId)
    # sig.save()


    # print(request.POST['SymbolTitle'])
    # print(newsignal)
    # return redirect('submit')
    signal_list = signal.objects.all().filter(IsActive=True).order_by('-id')
    context ={'signal_list': signal_list,'frm': form}
    
    
    # return render(request,'signals/update.html',context)
    return render(request, "signals/update.html", context)
