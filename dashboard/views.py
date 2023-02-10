from django.shortcuts import render,redirect
from .monitor import *
import asyncio
import threading
from asgiref.sync import sync_to_async
from django_q.tasks import async_task
# Create your views here.
def userdashboard(request):
    return render(request,'dashboard/index.html')

def status(request):
    return render(request,'dashboard/status.html')

def dashabout(request):
    return render(request,'dashboard/dash_about.html')


def uploadTxt(request):
    if request.method=='POST':
        user_id = request.user.id
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
        t1 = threading.Thread(target=websiteChecking(user_id,final_urls,w_url,checking_time,alert_time), name='t1')
        t1.start()
        context = {'websites_list': websites_list}
        # async_task(websiteChecking, user_id,final_urls,w_url,checking_time,alert_time)
        return render(request, 'dashboard/status.html', context=context)

        
        
        
