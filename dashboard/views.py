from django.shortcuts import render

# Create your views here.
def userdashboard(request):
    return render(request,'dashboard/index.html')