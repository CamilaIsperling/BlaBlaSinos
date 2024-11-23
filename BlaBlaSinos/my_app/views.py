from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')  # Certifique-se de que o caminho está correto
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')  # atualmente redirecionando para a landing page
        else:
            messages.error(request, "Usuário não encontrado.")
            
    return render(request, 'login.html')  # Certifique-se que 'login.html' está na pasta templates

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'O nome de usuário já existe')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'O e-mail já está cadastrado')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Conta criada com sucesso')
                return redirect('login')
        else:
            messages.error(request, 'As senhas não coincidem')
            
    return render(request, 'register.html')

def caronas(request):
    return render(request, 'index_carona.html')

def cadastrarCaronas(request):
    return render(request, 'index_motorista.html')