# Introdução

Analise o seguinte problema hipotético:

"Foi verificado que a empresa não está tendo a quantidade de vendas que esperava em relação aos seus produtos mais vendidos, que são notebooks, smartphones, tablets, headsets e consoles. Com suspeitas de que as E-commerce rivais tenham uma vantagem atrativa em relação aos preços, faz-se necessário verificar esses preços para conferir se há ou não essa vantagem e qual o tamanho dela. O objetivo seria construir uma pipeline para coletar dados de produtos em um site de e-commerce."

Tendo o problema em mente, vamos às soluções.

## Setup e instruções para rodar:

Antes de tudo, entenda que esse projeto foi feito para rodar no Linux ou WSL (no caso do Windows). Certifique-se de que está clonando ele em uma pasta do Linux.

1. Instale o Docker (+ Docker Compose)
2. Insira o comando `git clone https://github.com/lucasrangelt/AdvancedProjectB---Scraping.git`
3. Insira o seguinte comando com o terminal aberto na pasta principal do projeto: `"mv .env.example .env; mv dbt_project/profiles.yml.example dbt_project/profiles.yml"` 
4. Insira o comando `docker compose up -d` com o terminal aberto na pasta principal do projeto (ou construa o container utilizando a ferramenta de sua preferência, como a extensão do VS Code)
5. Defina um horário de funcionamento diário no arquivo dags/scrapy_pipeline.py, ou abra a interface do Airflow no seu navegador (endereço: http://localhost:8081/), insira "airflow" como nome de usuário e password (o ideal seria mudar essas credenciais depois) vá em dags e rode o scraper manualmente.

# Ferramentas Escolhidas

- Usei **VS Code** como meu IDE para programar em várias linguagens como **Python**, **Yaml**, **Jinja** e **SQL**.
- Usei **WSL2** (ambiente virtual do Linux) para armazenar meu projeto, devido a velocidade superior e ao fato de ser o motor nativo do Docker.
- Usei **Docker** para resolver problemas de dependências locais e globais, além de possibilitar que o sistema seja executado em qualquer máquina.
- Usei **PostgreSQL** como base de dados para armazenar as informações coletadas dos produtos através do Scrapy.
- Usei **DBeaver** para visualizar minhas bases de dados locais e da nuvem.
- Usei **Python** para programar os arquivos do Scrapy, Airflow, entre outros.
- Usei **Scrapy** para coletar os dados de diferentes sites.
- Usei **SQL** para criar minhas bases de dados.
- Usei **Data Build Tool (dbt)** para modelar e manipular dados em arquitetura Medallion e criar uma Star Schema.
- Usei **Great Expectations** a fim de garantir a qualidade dos dados a serem inseridos na tabela final.
- Usei **Airflow** para orquestrar e executar em horário fixo múltiplas tarefas dependentes entre si, buscando saber onde e como qualquer delas pode vir a falhar.
- Usei **GitHub** para subir meu projeto e torná-lo acessível a todos.
- Usei **GitHub Actions** para garantir que o código funcione sem erros de digitação e/ou integração, trazendo assim a CI/CD (integração e desenvolvimento contínuo) para o projeto.
- Usei **.env**, **GitHub Secrets** e **AWS Secrets Manager** para garantir a segurança das minhas credenciais.
- Usei **AWS** e suas ferramentas de **RDS, ECS/Fargate, ECR, IAM**, entre outros para subir e manter minha base de dados na nuvem, e garantir que o projeto possa rodar de forma remota.
- Usei **Google Gemini** como ferramenta de auxílio para solucionar alguns erros de sintaxe e fazer a depuração (debug) de alguns erros/logs. Também usei para entender os vários usos e aplicações das ferramentas aplicadas.

**Meu e-mail: lucasrangel2011@gmail.com**

**Meu LinkedIn: https://www.linkedin.com/in/lucas-rangel-tietbohl-29791237b/**

Para ver o passo-a-passo do processo de desenvolvimento e minha jornada de aprendizado assim como os créditos, referências e alguns extras, confira o [Journal](JournalPT.md)