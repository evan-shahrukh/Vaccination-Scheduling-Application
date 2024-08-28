from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "message" : "Hello , World!"
    }
    return render(request,"./mysite/index.html",context)
    # return HttpResponse("<h2>Hello , World!</h2>")