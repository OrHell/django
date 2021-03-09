from django.shortcuts import render

# Create your views here.
def search_page(request):
    a='Testovaya stroka '
    context = {
        'test' :a,
    }
    return render(request, 'first_page.html',context)