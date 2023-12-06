from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def facebook(request):
    hai = 'Hii welcome to Facebook login page'
    data ={'name':'Narendra Sai','h':hai,}

    return render(request,'facebook.html',context=data)

def instagram(request):
    
    return HttpResponse('<center><h1 style="color: darkgoldenrod;"> Haii Narendra Sai welcome to Instagram login Page')

def whatsapp(request):
    data='Good to see you friend...!'
    d={'welcome':data,'name':'Sai Narendra reddy'}
    
    return render(request,'whatsapp.html',context=d)