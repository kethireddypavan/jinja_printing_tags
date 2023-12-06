from django.shortcuts import render

# Create your views here.
def linkdin(request):
    data = 'Haii hope you are doing well'
    d={'welcome':data,'name':'Narendra Reddy'}

    return render(request,'linkdin.html',context=d)

def telegram(request):
    data='This is the Data that we have fetched from the Database to Backend and displayed on Frontend page '
    d={'name':'Kagithala Narendra Sai Reddy','welcome':data,}

    return render(request,'telegram.html',context=d)