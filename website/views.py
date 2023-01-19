from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
# Create your views here.

def base(request):
    #temp=loader.get_template('htmlfiles\main.html')
    return render(request, 'website/base.html')

def home(reqeust):
    return render(reqeust, 'website/home.html')