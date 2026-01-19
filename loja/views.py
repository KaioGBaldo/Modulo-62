import time
import threading
from django.http import HttpResponse


def tarefa_lenta():
    """
    Função que simula uma tarefa custosa.
    Representa processamento pesado ou I/O bloqueante.
    """
    time.sleep(3)


def execucao_sincrona(request):
    """
    Executa as tarefas de forma sequencial (sem concorrência).
    """
    inicio = time.time()

    for _ in range(3):
        tarefa_lenta()

    fim = time.time()
    tempo_total = fim - inicio

    return HttpResponse(
        f"Tipo de execução: Sincrona\n"
        f"Tempo de execução: {tempo_total:.2f} segundos"
    )


def execucao_concorrente(request):
    """
    Executa as tarefas de forma concorrente utilizando threads.
    """
    inicio = time.time()

    threads = []

    for _ in range(3):
        thread = threading.Thread(target=tarefa_lenta)
        thread.start()
        threads.append(thread)

    # Aguarda todas as threads finalizarem
    for thread in threads:
        thread.join()

    fim = time.time()
    tempo_total = fim - inicio

    return HttpResponse(
        f"Tipo de execução: Concorrente\n"
        f"Tempo de execução: {tempo_total:.2f} segundos"
    )
