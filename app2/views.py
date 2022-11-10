from django.shortcuts import render
from multiprocessing import context

def Apple(request):
    Products=['iPhone 1','iPhone 2','iPhone 7','iPhone 11','iPhone 12','iPhone 13','iPhone 13 pro','iPhone 13 pro max']
    context={'Products': Products}
    return render(request,'app2/Apple.html',context)

def Realme(request):
    Products=['Realme C1','Realme C2','Realme c3','Realme C7','Realme 5','Realme 5s','Realme C21']
    context={'Products': Products}
    return render(request,'app2/Realme.html',context)

# Create your views here.
def oneplus(request):
    Products=['oneplus2','oneplus3','oneplus5','oneplus5T','oneplus6','oneplus8','oneplus9t','oneplus10']
    context={'Products': Products}
    return render(request,'app2/oneplus.html',context)