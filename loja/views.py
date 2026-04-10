import asyncio
import httpx
from django.http import HttpResponse

async def home_async(request):
    print("Iniciando a view assíncrona...")
    
    # Em vez de apenas esperar 2 segundos parado, vamos contar:
    for i in range(1, 6): # Vai contar de 1 até 5
        await asyncio.sleep(1) # Espera 1 segundo sem travar o servidor
        print(f"Passaram-se {i} segundos...")
    
    print("Trabalho finalizado no terminal!")
    return HttpResponse("Resposta Assíncrona: Finalizada com sucesso!")

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
