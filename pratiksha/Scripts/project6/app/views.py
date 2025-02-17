from django.shortcuts import render

# Create your views here.
def image_instr(request):
    return render(request,'image_instr.html')