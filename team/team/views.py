from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return render(request,'one.html')
state=''
def second(request):
    global state
    state=request.GET.get('state')
    params={'sname':state}
    return render(request,'second.html',params)
def third(request):
    disease=request.GET.get('submit')
    params={'sname':state,'scheme':disease}
    return render(request,'third.html',params)