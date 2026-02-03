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

Day 4: I worked to integrate all of the core infrastructure (Windows, WSL2, VS Code, ~~.venv~~, Docker, GitHub and PostgreSQL).

Day 5: Finished integrating the core infrastructure, fixing bugs and mapping errors on the GitHub repository.

Day 6: Integrated the scraper and Dbeaver with Docker's PostgreSQL.

![dbeaver-database-vscode](imgs/2-dbeaver-database-vscode.png)

Day 7: Organized, tested Organizei, testei e corrigi bugs no scraper.

Dia 8: Planned, updated and tested the scraper. I also installed the dbt and Great Expectations libraries.

![vscode-dbt-profiles](imgs/3-vscode-dbt-profiles.png)

Day 9: I planned and created paths for dbt and used the tool in order to organize data and implement a Star Schema.

![database-medallion](imgs/4-database-medallion.png)

Day 10: Implemented Great Expectations from beginning to end.

Day 11: Fixed bugs and errors on Great Expectations.

![vscode-gx-validation](imgs/5-vscode-gx-validation.png)

Day 12: Started to prepare Airflow's infrastructure.

Day 13: Fixed bugs and finished installing Airflow's infrastructure and started connecting it to other tools.

Day 14: Kept trying to implement Airflow using the version 2.7.1 template.

Day 15: I swapped my Airflow template for the official 3.1.5 one. Then, I finished implementing Airflow.

![docker-airflow](imgs/6-docker-airflow.png)

![airflow-ui](imgs/7-airflow-ui.png)

Day 16: Fixed my credentials, making them secret with the .env file and started to implement GitHub Actions for CI/CD.

Day 17: Fixed credential reference errors and finished implementing GitHub Actions.

Day 18: I planned and fought permission errors on Azure due to my university account. Couldn't create a normal account.

Day 19: I planned, explored AWS and began preparations to upload the project to the cloud.

Day 20: I created the whole cloud infrastructure and uploaded my scraper to the AWS ECR. I also integrated Airflow with AWS.

Day 21: Created a PostgreSQL database on the cloud and fixed key and passwords mapping.

Day 22: Fixed the main bugs, permission errors, etc. effectively concluding the pipeline and the main project.

![aws-rds-services](imgs/8-aws-rds-services.png)

Day 23: Fixed silent bugs and decided to make Scrapy run locally in order to avoid private proxies.

Day 24: Scaled the scraper, changing code to scrape 5 items and also added new scrapers for more websites.

Day 25: Gathered information to work on the ReadMe.md file and ensure a good project presentation.

Day 26: Fought "anti-bot" errors in multiple websites on scrapy; updated my ReadMe.md and gathered images for visualizations.

Day 27: Finished coding my ReadMe.md, concluding the project presentation.

Day 28: Ensured the exclusion of duplicated items on dbt, though I also eased data collection for "price over time".

Day 29: Upgraded GX to warn me on Discord whenever there is a small error, instead of stopping the whole pipeline.

Day 31: Changed my Airflow port from "8080:8080" to "8081:8080" due to browser endless-loading errors.

Extra: Internationalized my ReadMe.md, translating the file from portuguese to english.

![pipeline-final-2026-01-27-0122](imgs/9-pipeline-final-2026-01-27-0122.png)

# Key Takes

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