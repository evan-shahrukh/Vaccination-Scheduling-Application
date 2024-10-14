from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.user.is_authenticated:
        return render(request,"./mysite/dashboard.html",context={"user" : request.user})
    context = {
        "message" : "Hello , World!"
    }
    return render(request,"./mysite/index.html",context)
    # return HttpResponse("<h2>Hello , World!</h2>")