# Introduction

Analyse the following hipothetical problem:

"It was verified that the company did not meet the forecasted sales of its most sold items, that are notebooks, smartphones, tablets, headsets and consoles. Suspecting that rival e-commerces might have an attractive advantage price-wise, it's necessary to verify these prices to see whether there is or not such advantage and what its size is. The objective here is to build a pipeline in order to collect product data from an e-commerce website."

Having the problem in mind, let's go to the solutions.

## Setup and instructions to run it:

1. Install Docker
2. Insert the command "docker compose up" with the terminal open on the project root folder (or build the containers using your preferred tool, like the VS Code extension)
3. Remove the ".example" from the .env.example and dbt_project/profiles.yml.example files
4. Change the .env comments to your credentials
5. Define a daily working time for the file dags/scrapy_pipeline.py, or open the Airflow interface on your browser (link: http://localhost:8081/), insert "airflow" as both username and password (ideally you should change these credentials later), go to "dags" and run the scraper manually.

# Chosen Tools

- I used **VS Code** as my programming IDE for many languages like **Python**, **Yaml**, **Jinja**, **SQL**, etc.
- I used **WSL2** (Windows Subsystem for Linux) as a place to sit my project, due to its superior speed and the fact that it is Docker's native engine.
- I used **Docker** in order to solve local and global dependency issues (dependency hell) and allow it to be executed on any machine.
- I used **PostgreSQL** as my database to store product data that is extracted from Scrapy.
- I used **DBeaver** in order to visualize both my local and cloud-based databases.
- I used **Python** in order to write files from Scrapy, Airflow and many others.
- I used **Scrapy** in order to collect data from multiple sites.
- I used **SQL** in order to write queries for my databases.
- I used **Data Build Tool (dbt)** to model, orchestrate and manipulate data in a Medallion Architecture and create a Star Schema.
- I used **Great Expectations** in order to ensure the quality of the data to be inserted on the final tables.
- I used **Airflow** to orchestrate and execute multiple interdependent tasks on fixed hour, seeking to know when and how any of them could come to fail.
- I used **GitHub** to upload my project for everyone's visibility and accessibility.
- I used **GitHub Actions** in order to ensure that my code will run with no typos and/or integration errors, therefore bringing CI/CD (Continuous Integration and Continuous Development) to the project.
- I used **.env**, **GitHub Secrets** and **AWS Secrets Manager** in order to ensure credentials security.
- I used **AWS** and its tools of **RDS, ECS/Fargate, ECR, IAM**, among others in order to upload and keep my database on the cloud, guaranteeing that the project could work remotely.
- I used **Google Gemini** as an auxiliary tool for solving typos, syntax errors and debugging bugs/logs. I also used it in order to understand the many different uses and applications of the chosen tools.

# Log and Development Process

Days before: I planned, studied and tried to understand how the architecture of a project works as a whole (macro vision).

Day 31/12: I planned and worked on Scrapy. I was also introduced to WSL2.

### System Architecture Diagram

![architecture-2026-01-25-1726](imgs/1-architecture-2026-01-25-1726.png)

Day 1: I planned and worked on scrapy, ~~integrated Playwright on the program~~ and also integrated WSL2 on VS Code.

Day 2: I planned, instalaled Docker, moved my project to \\wsl$ and remapped the GitHub repository to the new project root folder.

Day 3: I planned, installed a virtual environment to avoid "dependency hell" and also installed Dec Containers for my extensions.

Dia 4: Trabalhei para integrar toda a principal infraestrutura (Windows, WSL2, VS Code, .venv, Docker, GitHub, PostgreSQL).

Dia 5: Terminei de integrar toda a principal infraestrutura, corrigindo bugs e erros de mapeamento no GitHub.

Dia 6: Integrei o scraper e DBeaver com o PostgreSQL do Docker.

![dbeaver-database-vscode](imgs/2-dbeaver-database-vscode.png)

Dia 7: Organizei, testei e corrigi bugs no scraper.

Dia 8: Planejei, editei, testei o scraper e instalei as bibliotecas de dbt e Great Expectations.

![vscode-dbt-profiles](imgs/3-vscode-dbt-profiles.png)

Dia 9: Planejei, criei pastas para o dbt e utilizei dbt para organizar dados e implementar uma Star Schema.

![database-medallion](imgs/4-database-medallion.png)

Dia 10: Implementei Great Expectations do começo ao fim.

Dia 11: Corrigi bugs e erros no Great Expectations.

![vscode-gx-validation](imgs/5-vscode-gx-validation.png)

Dia 12: Comecei a preparar a infraestrutura do Airflow.

Dia 13: Corrigi bugs e terminei de instalar a infraestrutura do Airflow e comecei a conectá-lo com as outras ferramentas.

Dia 14: Continuei tentando implementar o Airflow usando a template da versão 2.0.

Dia 15: Troquei a minha template do Airflow pela oficial da versão 3.1.5. Terminei de implementar o Airflow.

![docker-airflow](imgs/6-docker-airflow.png)

![airflow-ui](imgs/7-airflow-ui.png)

Dia 16: Corrigi minhas credenciais e tornei elas secretas com o arquivo .env e comecei a implementar Github Actions para CI/CD.

Dia 17: Corrigi erros de referência de credenciais e terminei de implementar GitHub Actions.

Dia 18: Planejei e enfrentei problemas de permissão no Azure devido a minha conta de universitário. Não consegui criar nova conta.

Dia 19: Planejei, explorei o AWS e comecei os preparativos para subir o projeto para a nuvem.

Dia 20: Criei toda a infraestrutura na nuvem e subi meu scraper para o ECR da AWS. Integrei o Airflow com a nuvem.

Dia 21: Criei uma base de dados PostgreSQL na nuvem e corrigi mapeamentos de chaves e passwords.

Dia 22: Corrigi os principais bugs, erros de permissões, etc. efetivamente concluindo a pipeline e o projeto principal.

![aws-rds-services](imgs/8-aws-rds-services.png)

Dia 23: Corrigi bugs silenciosos e resolvi fazer o Scrapy executar de forma local para evitar proxies.

Dia 24: Escalei o scrapy, mudando o código para fazer scraping de 5 itens e adicionei novos scrapers para mais sites.

Dia 25: Reuni informações para trabalhar no arquivo ReadMe.md e garantir uma boa apresentação do projeto.

Dia 26: Enfrentei erros "anti-bots" em vários sites no scrapy; atualizei meu ReadMe.md e coletei imagens para visualizações.

Dia 27: Conclui meu arquivo ReamMe.md, terminando a apresentação do projeto.

Dia 28: Garanti a exclusão de itens duplicados no dbt, ao mesmo tempo que facilitei a coleta de dados como "preço ao longo do tempo".

Dia 29: Melhorei o GX para dar um aviso no Discord quando em caso de um erro pequeno, em vez de parar a pipeline inteira.

![pipeline-final-2026-01-27-0122](imgs/9-pipeline-final-2026-01-27-0122.png)

# Aprendizados

Aprendi a desenvolver uma pipeline de dados do começo ao fim utilizando ferramentas padrão de indústria para resolver cada uma das partes do sistema. Algumas ferramentas eu já tinha experiência, mas a maioria delas era novidade para mim. Apesar disso, consegui desenvolver bem as minhas ideias, graças ao vários recursos que busquei. Entre os vários aprendizados que obtive, eis os principais que poderão me ajudar para eventos futuros:

- Aprendi várias templates de arquivos como Dockerfile, docker-compose.yml, main.yml, DAG.py, etc.
- Não "forçar" a template da versão de uma ferramenta para outra versão.
- Focar na segurança, arquitetura e infraestrutura do projeto primeiro e apenas depois na sintaxe das ferramentas.
- Aprendi como funciona todo o ciclo de uma pipeline, o processo de coleta (API Endpoint/Scrapy/outras possíveis ferramentas), modelagem (dbt), qualidade (GX), armazenamento (PostgreSQL/RDS), orquestramento (Airflow), etc.
- Sempre começar um projeto utilizando .env quando necessário, em vez de implementar depois.
- Aprendi a não me importar com "marcas" e sim com a entrega do projeto. Quando a Azure me rejeitou (3 vezes), fui para a competição para garantir continuidade.
- Ao criar uma base de dados no AWS, apenas uma instância será criada. O nome dela será postgres, apesar de algum outro nome escolhido. Para resolver isso, deve-se entrar no DBeaver (ou na ferramenta de visualização utilizada), conectar-se à instância na nuvem e criar uma com o nome desejado.
- No final, escolhi puxar o meu scraper de volta para o ambiente local, pois caso contrário iria ter que pagar proxies privadas para fazer scraping. O Airflow também ficou na minha máquina local, visto que iria ser desnecessariamente caro ter uma ferramenta tão complexa e pesada rodando em nuvem.

# Créditos e Referências

![2026-01-02-Google-Gemini-1](imgs/creditos/2026-01-02-Google-Gemini-1.png)
![2026-01-02-Google-Gemini-2](imgs/creditos/2026-01-02-Google-Gemini-2.png)
---
---
---
![2026-01-07-at-18-11-14-AddyOsmani](imgs/creditos/2026-01-07-at-18-11-14-AddyOsmani.png)
---
---
---
![2026-01-08-at-12-31-03-Google-Gemini](imgs/creditos/2026-01-08-at-12-31-03-Google-Gemini.png)
---
---
---
![2026-01-12-at-23-32-16-ProgrammerHumor](imgs/creditos/2026-01-12-at-23-32-16-ProgrammerHumor.png)
![2026-01-12-at-23-32-28-ProgrammerHumor](imgs/creditos/2026-01-12-at-23-32-28-ProgrammerHumor.png)
![2026-01-13-at-00-03-10-ProgrammerHumor](imgs/creditos/2026-01-13-at-00-03-10-ProgrammerHumor.png)
---
---
---
![2026-01-19-at-11-27-25-brdev](imgs/creditos/2026-01-19-at-11-27-25-brdev.png)
---
---
---
![2026-01-21-at-02-35-27-Google-Gemini](imgs/creditos/2026-01-21-at-02-35-27-Google-Gemini.png)

### Links

- Projeto Tutorial de Python: https://github.com/lucasrangelt/PYTHONproject
- Projeto Tutorial de SQL: https://github.com/lucasrangelt/SQLcourse
- Plataforma de Diagramação: https://excalidraw.com/
- Instalando o Docker: https://www.youtube.com/watch?time_continue=1599&v=lP8xXebHmuE&embeds_referring_euri=https%3A%2F%2Fgemini.google.com%2F&embeds_referring_origin=https%3A%2F%2Fgemini.google.com&source_ve_path=Mjg2NjY
- Tutorial de Airflow/AWS: https://www.youtube.com/watch?v=o88LNQDH2uI
- Tutorial para Instalar Airflow no Docker: https://www.youtube.com/watch?v=ma8OuIz-ai0
- Airflow 3.1.5 (Documentação): https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
- Para referências e Debug: https://www.startdataengineering.com/
- Curso de Engenharia de Dados da IBM: https://www.coursera.org/professional-certificates/ibm-data-engineer
---
---
---
### Links do Gemini

- Tactical Executions: https://gemini.google.com/share/9b04f1af5a43
- Implement the things you need to learn: https://gemini.google.com/share/860923366ed0
- What is each thing: https://gemini.google.com/share/68a31589e27b
- Dbt Source YAML Comparison: https://gemini.google.com/share/1272ec020734
- Data Engineering and Web Scraping Frequency: https://gemini.google.com/share/4834319f82fd

### Uso da IA

Neste projeto, eu descobri o que significa usar a inteligência artificial como ferramenta de desenvolvimento na prática. Apesar da IA ajudar com algumas sugestões, se não forem ideais e o desenvolvedor aceitar e se aprofundar nelas, o controle do "leme" pode ser perdido.

A IA é como aquele veterano de guerra que, devido à idade, pode acabar "aumentando" ou "trocando as coisas de espaço temporal". Por exemplo, ele pode começar a falar sobre como "a Alemanha Oriental é um país ultrapassado, que vai contra a democracia e os direitos dos seus cidadãos", e aí você lembra ele de que a Alemanha se unificou há mais de 30 anos e ele responde com "Você está absolutamente certo!!" e começa a concordar e a contar coisas. Ele tem muito a ensinar, mas quem está ouvindo deve ter ou um pouco de conhecimento prévio, ou um lugar seguro para testar o que foi ouvido antes de sair espalhando informação desatualizada.

Na maioria dos casos que a IA "alucinou" foi em relação às interfaces de usuário (UI), como DBeaver, o que faz sentido, pois é mais fácil para ela trabalhar com elementos de texto e lógica do que botões em uma tela que ela não consegue ver. Teve uma vez, na hora de eliminar a branch "master" que havia sido criada, a IA me sugeriu um código que parecia certo no começo, mas puxou o meu projeto em uma semana de progresso. Claro que eu percebi isso no comando e fiz backup logo antes de executar. Nenhum dano ocorreu no final. Discernimento é extremamente necessário para se trabalhar com IA.

Se a IA não "te dá a resposta que você quer", é praticamente 100% por causa do jeito que a questão foi formulada: Se você esquecer alguma coisa ou deixar muito vago, a resposta pode não vir muito bem detalhada. Isso pode ser ruim para problemas específicos, ou bom para quem quer sugestões iniciais. Se exagerar nos detalhes, pode-se receber a resposta para 5 ou 6 tipos de problemas quando mal se tem acesso a um deles. Trabalhar com a IA me ensinou jeitos otimizados de se fazer perguntas para resolver problemas.

Ressaltando que, apesar das várias boas sugestões que recebi, no final eu soube assumir o controle e filtrar as que não me agradava. Eis a seguir algumas dessas sugestões (que também provavelmente serão encontradas em algum lugar da conversa "Tactical Executions"):

- IA me sugeriu utilizar o BeautifulSoup. Após comparar, escolhi o Scrapy, visando escalabilidade e performance.
- IA sugeriu que eu fizesse scraping apenas de um site, mas construi outros scrapers para confirmar a escalabilidade.
- IA sugeriu colocar o "docker-compose.yml" dentro da .devcontainers. Segui a sugestão, mas acabei puxando para a root depois.
- IA sugeriu colocar minhas credenciais nos scripts python (clássico). Eu usei .env devido aos riscos de segurança. 
- IA sugeriu Airflow 2.7.1. Eu escolhi Airflow 3.1.5 por ser mais atualizado.
- IA sugeriu sintaxe desatualizada para importar dependências no GX. Verifiquei a documentação e atualizei o código.
- Decidi deletar todas as minhas imagens e volumes (menos o Postgres) e reconstruir para ver se funcionava normal.
- IA me sugeriu seguir Scrapy >>> dbt (tabela final) >>> GX no Airflow. Escolhi Scrapy >>> dbt (tabela stg) >>> GX >>> dbt (tabela final) para filtrar dados antes de carregar.
- IA me sugeriu usar o termo "prod" no GitHub Actions. Preferi usar o target "ci" por parecer mais apropriado.
- IA me sugeriu usar variáveis env como "DB_USER". Escolhi "ENV_USER" pela relação próxima com códigos relacionados.
- IA me sugeriu usar um comando bash para instalar AWS CLI para meu aplicativo em container. Escolhi instalar no Dockerfile.
- IA me sugeriu restringir para que apenas minha "main" branch publicasse no AWS. Permiti todas, a fim de testar possibilidades.

**Meu e-mail: lucasrangel2011@gmail.com**

**Meu LinkedIn: https://www.linkedin.com/in/lucas-rangel-tietbohl-29791237b/**