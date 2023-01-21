from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='website-home'),
    #path("simple_function",view.simple_function)
    path('about/',views.about,name='website-about'),
]