from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Certifique-se de que o caminho está correto
    
def login_view(request):
    return render(request, 'login.html')  # Certifique-se que 'login.html' está na pasta templates
