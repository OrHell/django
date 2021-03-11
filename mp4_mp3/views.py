from django.shortcuts import render

# Create your views here.

def home_convert_page(request):
     context = {

     }
     return render(request, 'convert_page.html',context )
