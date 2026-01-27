# Introdução

Analise o seguinte problema hipotético:

"Foi verificado que a empresa não está tendo a quantidade de vendas que esperava em relação aos seus produtos mais vendidos, que são notebooks, smartphones, tablets, headsets e consoles. Com suspeitas de que as E-commerce rivais tenham uma vantagem atrativa em relação aos preços, faz-se necessário verificar esses preços para conferir se há ou não essa vantagem e qual o tamanho dela. O objetivo seria construir uma pipeline para coletar dados de produtos em um site de E-commerce."

Tendo o problema em mente, vamos às soluções.

# Ferramentas Escolhidas

- Usei **VS Code** como meu IDE para programar em várias linguagens como **Python**, **Yaml**, **Jinja**.
- Usei **WSL2** (ambiente virtual do Linux) para armazenar meu projeto, devido a velocidade superior e ao fato de ser o motor nativo do Docker.
- Usei **Docker** para resolver problemas de dependências locais e globais, além de possibilitar que o sistema seja executado em qualquer máquina.
- Usei **PostgreSQL** como base de dados para armazenar as informações coletadas dos produtos através do Scrapy.
- Usei **DBeaver** para visualizar minhas bases de dados locais e da nuvem.
- Usei **Python** para programar os arquivos do Scrapy, Airflow, entre outros.
- Usei **Scrapy** para coletar os dados de diferentes sites.
- Usei **SQL** para criar minhas bases de dados.
- Usei **Data Build Tool (dbt)** para modelar, orquestrar, manipular dados em arquitetura Medallion e criar uma Star Schema.
- Usei **Great Expectations** a fim de garantir a qualidade dos dados a serem inseridos na tabela final.
- Usei **Airflow** para orquestrar e executar em horário fixo múltiplas tarefas dependentes entre si, buscando saber onde e como qualquer delas pode vir a falhar.
- Usei **GitHub** para subir meu projeto e torná-lo acessível a todos.
- Usei **GitHub Actions** para garantir que o código funcione sem erros de digitação e/ou integração, trazendo assim a CI/CD (integração e desenvolvimento contínuo) para o projeto.
- Usei **.env**, **GitHub Secrets** e **AWS Secrets Manager** para garantir a segurança das minhas credenciais.
- Usei **AWS** e suas ferramentas de **RDS, ECS/Fargate, ECR, IAM**, entre outros para subir e manter minha base de dados na nuvem, e garantir que o projeto possa rodar de forma remota.

# Log e Processo de Desenvolvimento

Dias anteriores: Planejei, estudei e tentei compreender como funciona a arquitetura de um projeto como um todo (visão macro).

Dia 31/12: Planejei, trabalhei no Scrapy e fui introduzido ao WSL2.

### Diagrama de Arquitetura do Sistema

![diagrama de arquitetura](imgs/1-arquitetura-2026-01-25-1726.png)

Dia 1: Planejei, trabalhei no Scrapy, ~~integrei Playwright ao programa~~ e integrei WSL2 ao VS Code.

Dia 2: Planejei, instalei o Docker, movi meu projeto para \\wsl$ e remapeei o repositório do GitHub ao novo local do projeto.

Dia 3: Planejei, instalei um ambiente virtual para evitar "dependency hell" e Dev Containers para minhas extensões.

Dia 4: Trabalhei para integrar toda a principal infraestrutura (Windows, WSL2, VS Code, .venv, Docker, GitHub, PostgreSQL).

Dia 5: Terminei de integrar toda a principal infraestrutura, corrigindo bugs e erros de mapeamento no GitHub.

Dia 6: Integrei o scraper e DBeaver com o PostgreSQL do Docker.

Dia 7: Organizei, testei e corrigi bugs no scraper.

Dia 8: Planejei, editei, testei o scraper e instalei as bibliotecas de dbt e Great Expectations.

Dia 9: Planejei, criei pastas para o dbt e utilizei dbt para organizar dados e implementar uma Star Schema.

Dia 10: Implementei Great Expectations do começo ao fim.

Dia 11: Corrigi bugs e erros no Great Expectations.

Dia 12: Comecei a preparar a infraestrutura do Airflow.

Dia 13: Corrigi bugs e terminei de instalar a infraestrutura do Airflow e comecei a conectá-lo com as outras ferramentas.

Dia 14: Continuei tentando implementar o Airflow usando a template da versão 2.0.

Dia 15: Troquei a minha template do Airflow pela oficial da versão 3.1.5. Terminei de implementar o Airflow.

Dia 16: Corrigi minhas credenciais e tornei elas secretas com o arquivo .env e comecei a implementar Github Actions para CI/CD.

Dia 17: Corrigi erros de referência de credenciais e terminei de implementar GitHub Actions.

Dia 18: Planejei e enfrentei problemas de permissão no Azure devido a minha conta de universitário. Não consegui criar nova conta.

Dia 19: Planejei, explorei o AWS e comecei os preparativos para subir o projeto para a nuvem.

Dia 20: Criei toda a infraestrutura na nuvem e subi meu scraper para o ECR da AWS. Integrei o Airflow com a nuvem.

Dia 21: Criei uma base de dados PostgreSQL na nuvem e corrigi mapeamentos de chaves e passwords.

Dia 22: Corrigi os principais bugs, erros de permissões, etc. efetivamente concluindo a pipeline e o projeto principal.

Dia 23: Corrigi bugs silenciosos e resolvi fazer o Scrapy executar de forma local para evitar proxies.

Dia 24: Escalei o scrapy, mudando o código para fazer scraping de 5 itens e adicionei novos scrapers para mais sites.

Dia 25: Reuni informações para trabalhar no arquivo ReadMe.md e garantir uma boa apresentação do projeto.

Dia 26: Enfrentei erros "anti-bots" em vários sites no scrapy; atualizei meu ReadMe.md e coletei imagens para visualizações.

# Galeria

![dbeaver-database-vscode](imgs/2-dbeaver-database-vscode.png)

![vscode-dbt-profiles](imgs/3-vscode-dbt-profiles.png)

![database-medallion](imgs/4-database-medallion.png)

![vscode-gx-validation](imgs/5-vscode-gx-validation.png)

![docker-airflow](imgs/6-docker-airflow.png)

![airflow-ui](imgs/7-airflow-ui.png)

![aws-rds-services](imgs/8-aws-rds-services.png)

![pipeline-final-2026-01-27-0122](imgs/9-pipeline-final-2026-01-27-0122.png)

# Aprendizados

Aprendi a desenvolver uma pipeline de dados do começo ao fim utilizando ferramentas padrão de indústria para resolver cada uma das partes do sistema. Algumas ferramentas eu já tinha experiência, mas a maioria delas era novidade para mim. Apesar disso, consegui desenvolver bem as minhas ideias, graças ao vários recursos que busquei. Abaixo, fiz algumas anotações que poderão me ajudar para eventos futuros:

**annotations file items here**

# Créditos e Referências

https://github.com/lucasrangelt/PYTHONproject
https://github.com/lucasrangelt/SQLcourse