from django.urls import path
from my_app import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Rota para a página de login
    path('register/', views.register_view, name='register'),
    path('', views.index, name='index'),
    path('index_carona/', views.caronas, name='index_carona'),
    path('index_motorista/', views.cadastrarCaronas, name='cadastrarCaronas')
]