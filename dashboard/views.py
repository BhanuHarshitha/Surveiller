from django.shortcuts import render,redirect
from .monitor import *
import asyncio
import threading
# Create your views here.
def userdashboard(request):
    return render(request,'dashboard/index.html')

def status(request):
    return render(request,'dashboard/status.html')

def dashabout(request):
    return render(request,'dashboard/dash_about.html')

async def uploadTxt(request):
    if request.method=='POST':
        user = request.user
        checking_time=request.POST['fader']
        alert_type=request.POST['optradios']
        w_url=request.POST.get('w_url')
        alert_time=request.POST['optradio1']
        file=request.FILES['file1'].readlines()
        final_urls = []
        for sing_url in file:
            s_url='{}'.format(sing_url.strip()).replace("b\'","").replace('\'',"")
            final_urls.append(s_url)
        # print(final_urls)
        websites_list = Dashboard.objects.filter(user=request.user)
        context = {'websites_list': websites_list}
        # t1 = threading.Thread(target=websiteChecking(request,final_urls,w_url,checking_time,alert_time), name='t1')
        # t1.start()
        asyncio.create_task(websiteChecking(request,final_urls,w_url,checking_time,alert_time))
        return render(request, 'dashboard/status.html', context=context)
        
        
        
