from django.shortcuts import render
from multiprocessing import context


def home(request):
    context={'msg':'Please select the Brand'}
    return render(request,'app1/home.html',context)

def Samsung(request):
    Products=['Samsung Pocket','Samsung F20','Samsung M21','Samsung J1','Samsung J2','Samsung J5','Samsung J7']
    context={'Products': Products}
    return render(request,'app1/samsung.html',context)

# Create your views here.
