from django.core.management.base import BaseCommand
from loja.models import Post

class Command(BaseCommand):
    help = 'Exibe o contador de postagens no terminal'

    def handle(self, *args, **kwargs):
        # Regra: Contar o total de objetos no modelo Post
        total = Post.objects.count()
        total_publicados = Post.objects.filter(status='publicado').count()

        # O retorno via terminal solicitado
        self.stdout.write(self.style.SUCCESS(f'--- RELATÓRIO DE POSTAGENS ---'))
        self.stdout.write(f'Total de posts: {total}')
        self.stdout.write(f'Posts publicados: {total_publicados}')
        self.stdout.write(self.style.SUCCESS('------------------------------'))
