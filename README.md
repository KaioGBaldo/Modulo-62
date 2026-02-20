# ⚡ Django Performance & Concurrency - Síncrono vs Concorrente

Este projeto demonstra a diferença de performance entre o processamento sequencial e o concorrente no ambiente **Django**. O foco principal foi a implementação de multithreading para otimizar tarefas bloqueantes e o refinamento da interface administrativa para uma gestão de dados eficiente.

---

# 📝 Resumo (Resume)
Neste projeto, desenvolvi um experimento prático para medir ganhos de eficiência no Back-End. Implementei duas abordagens de execução: uma **síncrona**, onde tarefas lentas acumulam tempo de espera, e uma **concorrente**, utilizando a biblioteca `threading` para disparar processos simultâneos, reduzindo o tempo total de resposta de ~9 segundos para ~3 segundos. Paralelamente, apliquei customizações avançadas no **Django Admin**, utilizando decoradores e configurações de visualização (`list_display`, `list_filter`, `search_fields`) para transformar o banco de dados em um painel de controle intuitivo.



## 🚀 Tecnologias e Ferramentas (Tech Stack)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Threading](https://img.shields.io/badge/Python-Threading-blue?style=for-the-badge)](https://docs.python.org/3/library/threading.html)

## 📋 Funcionalidades em Destaque
* **Execução Concorrente com Threads:** Implementação de `threading.Thread` para realizar tarefas em paralelo, otimizando o I/O bloqueante da aplicação.
* **Benchmarking Síncrono:** Criação de endpoints para comparação de tempo real de execução utilizando o módulo `time`.
* **Customização do Django Admin:** Uso de `@admin.register` para criar interfaces de busca, filtragem e exibição de colunas personalizadas para Produtos e Estoque.
* **Busca Relacional:** Configuração de `search_fields` com suporte a campos estrangeiros (`produto__nome`), permitindo buscas inteligentes no estoque.
* **Arquitetura ASGI/WSGI:** Configurações prontas para lidar com diferentes protocolos de servidor e concorrência.
* **Internacionalização Avançada:** Ajuste completo para `pt-br` e fuso horário brasileiro, garantindo a precisão dos logs de criação de produtos.



---

# 👨‍💻 Sobre mi (About Me)
Olá, meu nome é **Kaio**, tenho 22 anos. Como meu foco principal é o **Back-End com Python**, entender como a concorrência funciona é o que me permite criar sistemas que suportam muitos usuários simultâneos. No Front-End com **React**, lidamos com o assincronismo do JavaScript; aqui no Back-End, aprendi a usar o hardware ao meu favor com as Threads do Python. Essa visão técnica me permite projetar sistemas que não apenas funcionam, mas são extremamente rápidos e fáceis de administrar.

### Entre em contato (Contact me)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=092E20)](https://linkedin.com/in/kaio-grativol-baldo-071a74150/)
[![Instagram](https://img.shields.io/badge/Instagram-000?style=for-the-badge&logo=instagram&logoColor=092E20)](https://www.instagram.com/kaiull__/)
[![GitHub](https://img.shields.io/badge/Github-000?style=for-the-badge&logo=github&logoColor=092E20)](https://github.com/SeuUsuarioAqui)

---
*Projeto desenvolvido para demonstrar proficiência em performance de back-end e administração avançada de sistemas com Django.*
