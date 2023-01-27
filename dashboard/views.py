from django.shortcuts import render

# Create your views here.
def userdashboard(request):
    return render(request,'dashboard/index.html')

def status(request):
    return render(request,'dashboard/status.html')

def dashabout(request):
    return render(request,'dashboard/dash_about.html')

def uploadTxtFile(request):
    if request.method == 'POST':
        file=request.FILES['file1'].readlines()
        duration=request.POST['fader']
        url=request.POST['w_url']
        alert=request.POST['alert_res']
        
        
        
