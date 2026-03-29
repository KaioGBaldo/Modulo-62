import asyncio
import httpx
from django.http import HttpResponse

# View Síncrona (Tradicional) - Apenas para comparação
def home_sync(request):
    import time
    time.sleep(2)  # Bloqueia o thread inteiro por 2 segundos
    return HttpResponse("Resposta Síncrona: Finalizada após 2s")

# View Assíncrona (O foco do seu exercício)
async def home_async(request):
    print("Iniciando a view assíncrona...")
    
    # Simulando uma chamada de API externa ou espera sem bloquear o servidor
    await asyncio.sleep(2) 
    
    # Exemplo opcional com httpx (mencionado no seu vídeo)
    # async with httpx.AsyncClient() as client:
    #     response = await client.get('https://www.google.com')
    
    print("Trabalho finalizado no terminal!")
    return HttpResponse("Resposta Assíncrona: Finalizada com sucesso!")
