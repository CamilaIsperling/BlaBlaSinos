from django.urls import path
from my_app import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Rota para a página de login
    path('', views.index, name='index')
]
