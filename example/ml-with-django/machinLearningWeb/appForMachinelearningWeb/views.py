from importlib.metadata import requires
from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def into(request):
    return render(request, 'into.html')