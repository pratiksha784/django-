from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'subject':'python','price':10000}
    return render(request,'jinjatext1.html',context=d)