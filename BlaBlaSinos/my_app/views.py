from django.shortcuts import render

def index(request):
    
    return render(request, 'my_app/templates/index.html')  # Certifique-se de que o caminho está correto
