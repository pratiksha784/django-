from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def paradisebiriyani(request):
    return HttpResponse("its very testy & delicious")
def dumbiriyani(request):
    return render(request,'dumbiriyani.html')