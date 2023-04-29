from django.shortcuts import render

# Create your views here.
def userdefinedfilter(request):
    d={'data':'hOw ArE YoU'}
    return render(request,'userdefinedfilter.html',d)
