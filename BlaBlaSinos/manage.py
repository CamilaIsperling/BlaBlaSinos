import os
import sys

def main():
    """Função principal para rodar as tarefas de gerenciamento do Django."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BlaBlaSinos.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar o Django. Verifique se ele está instalado e "
            "acessível no seu ambiente de desenvolvimento."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
