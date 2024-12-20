from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .models import Carona

def index(request):
    return render(request, 'index.html') 
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')  
        else:
            messages.error(request, "Usuário não encontrado.")
            
    return render(request, 'login.html')  

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
    caronas = Carona.objects.all().order_by('-created_at')[:5]
    return render(request, 'index_carona.html', {'caronas': caronas})

def cadastrarCaronas(request):
    if request.method == 'POST':
        origem = request.POST.get('origem')
        destino = request.POST.get('destino')
        passageiros = request.POST.get('passageiros')
        valor = request.POST.get('preco')
        horario_saida = request.POST.get('horario_saida')  
        horario_chegada = request.POST.get('horario_chegada')  

        if origem and destino and passageiros and valor and horario_saida and horario_chegada:
            carona = Carona(
                origem=origem, 
                destino=destino, 
                passageiros=passageiros, 
                valor=valor, 
                horario_saida=horario_saida,  
                horario_chegada=horario_chegada 
            )
            carona.save()
            return redirect('index_carona')
        else:
            return render(request, 'index_motorista.html', {'error': 'Preencha todos os campos!'})
    return render(request, 'index_motorista.html')

def listar_caronas(request):
    query = request.GET.get('search') 
    caronas = Carona.objects.all()

    if query:
        caronas = caronas.filter(origem__icontains=query)
        caronas = caronas.filter(destino__icontains=query)

    return render(request, 'index_carona.html', {'caronas': caronas})

def seguranca(request):
    return render(request, 'index_seguranca.html') 