import asyncio
import httpx
from django.http import HttpResponse

# View Síncrona (Tradicional) - Para comparação
def home_sync(request):
    import time
    # Bloqueia o thread inteiro. Ninguém mais entra enquanto não acabar.
    time.sleep(2)  
    return HttpResponse("Resposta Síncrona: Finalizada após 2s")

# View Assíncrona (O foco do seu exercício)
async def home_async(request):
    print("Iniciando a view assíncrona...")
    
    # Este loop atende ao pedido do professor: mostra a contagem no terminal
    for i in range(1, 6): 
        # O 'await' libera o servidor para outras tarefas enquanto espera
        await asyncio.sleep(1) 
        print(f"Contador: {i} segundos...")
    
    # Exemplo opcional com httpx (caso queira testar uma chamada real depois)
    # async with httpx.AsyncClient() as client:
    #     response = await client.get('https://www.google.com')
    
    print("Trabalho finalizado no terminal!")
    return HttpResponse("Resposta Assíncrona: Finalizada com sucesso!")