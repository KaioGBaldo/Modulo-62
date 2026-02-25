import time
from django.http import HttpResponse

def contador_terminal(request):
    # O professor quer ver estes prints no seu terminal
    print("\n" + "="*30)
    print("INICIANDO CONTAGEM MÓDULO 62")
    print("="*30)
    
    for i in range(1, 11):
        print(f">>> Número: {i}")
        time.sleep(1) # Pausa de 1 segundo entre os números
        
    print("="*30)
    print("CONTAGEM FINALIZADA")
    print("="*30 + "\n")
    
    return HttpResponse("<h1>Sucesso!</h1><p>A contagem de 1 a 10 foi realizada no terminal do VS Code.</p>")
