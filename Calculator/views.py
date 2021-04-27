from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello World")
    return render(request,'index.html')

def result(request):
    first = int(request.POST.get('first-Number','0'))
    second =int(request.POST.get('second-Number','0'))
    sum = str(first+second)
    dict = {"Sum":sum}
    return render(request,'result.html',dict)