from django.shortcuts import render

# Create your views here.
def cuenta(request):
    context={}
    return render(request,'usuario/cuenta.html',context)