from django.shortcuts import render

# Create your views here.

def home(request):
    #temp=loader.get_template('htmlfiles\main.html')
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')