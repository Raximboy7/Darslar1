from django.shortcuts import render

# Create your views here.
def index(request):
    tex = {}
    return render(request,'index.html',tex)