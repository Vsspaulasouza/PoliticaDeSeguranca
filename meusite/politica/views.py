from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request,'index.html')


def politica(request):
    return render(request, 'politica.html')

def chatbot(request):
    return redirect('https://127.0.0.1:9000/')



