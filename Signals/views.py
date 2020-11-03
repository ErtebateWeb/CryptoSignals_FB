from django.shortcuts import render
from django.http import HttpResponse
from .models import signal
 
# Create your views here.
def index(request):
    signal_list = signal.objects.all().filter(IsActive=True).order_by('-id')
    context ={'signal_list': signal_list}
    return render(request,'signals/index.html',context)




def home(request):
    qs = signal.objects.all()
    context = {
        "objects": qs
    }
    print(context)
    return render(request, "signals/signal_list.html", context)



# def submit_signal(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('signals/signal_list.html')
#     else:
#         form = PostForm()
#     return render(request, 'submit_signal.html', {'form': form})