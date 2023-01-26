from django.shortcuts import render

# Create your views here.
def userdashboard(request):
    return render(request,'dashboard/index.html')

def status(request):
    return render(request,'dashboard/status.html')