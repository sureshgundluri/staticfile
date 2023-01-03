from django.shortcuts import render

# Create your views here.
def staticfile(request):
    return render(request,'staticfile.html')