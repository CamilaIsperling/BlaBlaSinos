from django.urls import path, include

urlpatterns = [
    path('', include('my_app.urls')),  # Certifique-se de que 'my_app' é o nome correto
]
