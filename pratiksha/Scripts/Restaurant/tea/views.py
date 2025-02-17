from django.shortcuts import render

# Create your views here.
def tea(request):
    return render(request,'flvrtea.html')