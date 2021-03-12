from django.shortcuts import render

# Create your views here.
# domin_color.html
def home_color_page(request):
     context = {

     }
     return render(request, 'domin_color.html',context )
