import time
from django.http import HttpResponse

def contador_terminal(request):
    # O professor quer ver isso aqui no terminal do VS Code:
    print("\n--- INICIANDO CONTAGEM SOLICITADA ---") 
    
    for i in range(1, 11):
        print(f"Passo: {i}") # Isso aparece no terminal
        time.sleep(1)        # Isso dá o efeito de "número por número"
        
    print("--- CONTAGEM FINALIZADA ---\n")
    return HttpResponse("Verifique o seu terminal para ver a contagem!")
