from multiprocessing import context
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hi I'm Home:)")
    context={
        "variable":"this is sent"
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')