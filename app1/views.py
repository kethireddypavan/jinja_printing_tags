from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def data_render(request):
    data = 'This is the data what we have assumption from backend to displayed on html page'
    d = {'assumption':data ,'name':'Nani',}
    return render(request,'data_render.html',context=d)

def india(request):
    team='Team india has performed Best in the 2023 ICC World cup  and went to finals match with Australia on sunday we wish to India has to lift the cup...!'
    dic = {'news':team ,'name':'Rohit',}
    return render(request,'india.html',context=dic)

def hai(request):

    return HttpResponse('<center><h1> Hai iam from Visakhapatnam welcome Home')