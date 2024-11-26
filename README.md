# BlaBlaSinos

**Sistema de gerenciamento de caronas da Unisinos**

## Descrição
BlaBlaSinos é uma aplicação desenvolvida com Django para facilitar o gerenciamento de caronas na universidade Unisinos, promovendo sustentabilidade e economia entre os usuários.

---

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados no seu ambiente de desenvolvimento:

- **Python** (versão 3.9 ou superior)
- **pip** (gerenciador de pacotes do Python)
- **virtualenv** (opcional, mas recomendado para isolar o ambiente do projeto)
- **Banco de Dados**: MYSQL ou outro conforme necessário.

---

## Passos para rodar o projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/CamilaIsperling/BlaBlaSinos.git
cd blablasinos
```

### 2. Criar e ativar o ambiente virtual 
```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/MacOS:
source venv/bin/activate
```

### 3. Instalar as dependências
Certifique-se de estar no diretório raiz do projeto. Em seguida, instale as dependências listadas no arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Configurar as migrações do banco de dados
Crie as migrações e aplique-as:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Rodar o servidor local
Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```
A aplicação estará disponível no navegador pelo endereço [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Estrutura do projeto
- **`manage.py`**: Arquivo principal para comandos administrativos.
- **`app/`**: Diretório principal do aplicativo Django.
- **`templates/`**: Arquivos HTML para renderização das páginas.
- **`static/`**: Arquivos estáticos como CSS, JavaScript e imagens.

---
## Time de desenvolvimento

- [Camila Isperling Machado](https://br.linkedin.com/in/camila-isperling-a652a7208)
- [Felipe Alles Garcia](https://www.linkedin.com/in/felipealles/)
- [Gustavo Coitinho](https://br.linkedin.com/in/gustavo-coitinho)
- [Rodrigo Ritzel Bernasconi](https://www.linkedin.com/in/rodrigo-bernasconi-53923a224/)