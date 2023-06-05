from django.shortcuts import render

# Create your views here.
def if_else(request):
    d={'name':'Sudhanshu Pandey','age':23}
    return render(request,'if_else.html',context=d)
