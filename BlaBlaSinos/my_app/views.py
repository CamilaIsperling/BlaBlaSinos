from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Certifique-se de que o caminho está correto
