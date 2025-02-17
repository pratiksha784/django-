from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sampl1(request):
    return render(request,'sampl1.html')
def sampl2(request):
    return render(request,'sampl2.html')

def sampl3(request):
    return render(request,'sampl3.html')
def sampl4(request):
    return HttpResponse("its not me but youuu...")