from django.db import models

class Pessoa(models.Model):
    TipoPessoa = [
        ('passageiro', 'Passageiro'),
        ('motorista', 'Motorista'),
    ]
    
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    registro_academico = models.CharField(max_length=50, blank=True, null=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    tipo_pessoa = models.CharField(max_length=10, choices=TipoPessoa)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome

class AgendamentoViagem(models.Model):
    Status = [
        ('agendado', 'Agendado'),
        ('em andamento', 'Em Andamento'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ]
    
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_viagem = models.DateTimeField()
    cidade_origem = models.CharField(max_length=100)
    bairro_origem = models.CharField(max_length=100)
    cidade_destino = models.CharField(max_length=100)
    bairro_destino = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=15, choices=Status, default='agendado')
    data_criacao = models.DateTimeField(auto_now_add=True)
    hhorario_saida = models.TimeField(default="00:00:00")
    horario_chegada = models.TimeField(default="00:00:00")

    def __str__(self):
        return f"Viagem {self.id} - {self.pessoa.nome}"

class Avaliacao(models.Model):
    viagem = models.ForeignKey(AgendamentoViagem, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)
    data_avaliacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Avaliação {self.id} - Nota {self.nota}"

class Pagamento(models.Model):
    MetodoPagamento = [
        ('cartao', 'Cartão'),
        ('dinheiro', 'Dinheiro'),
        ('pix', 'PIX'),
    ]
    
    agendamento = models.ForeignKey(AgendamentoViagem, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    metodo_pagamento = models.CharField(max_length=10, choices=MetodoPagamento)
    
    def __str__(self):
        return f"Pagamento {self.id} - {self.metodo_pagamento}"

class HistoricoViagem(models.Model):
    agendamento = models.ForeignKey(AgendamentoViagem, on_delete=models.CASCADE)
    data_viagem = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    passageiro = models.ForeignKey(Pessoa, related_name='historico_passageiro', on_delete=models.CASCADE)
    motorista = models.ForeignKey(Pessoa, related_name='historico_motorista', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Histórico de Viagem {self.id}"

class Mensagem(models.Model):
    remetente = models.ForeignKey(Pessoa, related_name='mensagens_enviadas', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(Pessoa, related_name='mensagens_recebidas', on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Mensagem {self.id} - De {self.remetente} para {self.destinatario}"

class ConfiguracaoUsuario(models.Model):
    usuario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    notificacoes = models.BooleanField(default=True)
    modo_noturno = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Configuração do Usuário {self.usuario.nome}"
    
class Carona(models.Model):
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    passageiros = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    horario_saida = models.TimeField()
    horario_chegada = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)  # Novo campo

    def __str__(self):
        return f'{self.origem} - {self.destino}'
