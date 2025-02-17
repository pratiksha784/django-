from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rasagulla(request):
    return HttpResponse("Rasagulla is an emotion for all odia")
def pahalrasagulla(request):
    return render(request,'pahalrasagulla.html')