# Introduction

Analyze the following hypothetical problem:

"It was verified that the company did not meet the forecasted sales of its most sold items, that are notebooks, smartphones, tablets, headsets and consoles. Suspecting that rival e-commerce might have a pricing advantage, it's essential to monitor these prices to see whether there is or not such advantage and what its size is. The objective here is to build a pipeline in order to collect product data from an e-commerce website."

Having the problem in mind, let's go to the solutions.

## Setup and instructions to run it:

1. Install Docker
2. Run the command "mv .env.example .env; mv dbt_project/profiles.yml.example dbt_project/profiles.yml" with the terminal open on the project root folder
3. Change the .env comments to your credentials
4. Insert the command "docker compose up" with the terminal open on the project root folder (or build the containers using your preferred tool, like the VS Code extension)
5. Define a daily working time for the file dags/scrapy_pipeline.py, or open the Airflow interface on your browser (link: http://localhost:8081/), insert "airflow" as both username and password (ideally you should change these credentials later), go to "dags" and run the scraper manually.

# Chosen Tools

- I used **VS Code** as my programming IDE for many languages like **Python**, **Yaml**, **Jinja**, **SQL**, etc.
- I used **WSL2** (Windows Subsystem for Linux) as a development environment, due to its superior speed and the fact that it is Docker's native engine.
- I used **Docker** to solve local and global dependency issues (dependency hell) and allow it to be executed on any machine.
- I used **PostgreSQL** as my database to store product data that is extracted from Scrapy.
- I used **DBeaver** to visualize both my local and cloud-based databases.
- I used **Python** to write files from Scrapy, Airflow and many others.
- I used **Scrapy** to collect data from multiple sites.
- I used **SQL** to write queries for my databases.
- I used **Data Build Tool (dbt)** to model and manipulate data with idempotency in a Medallion Architecture and create a Star Schema.
- I used **Great Expectations** in order to ensure the quality of the data to be inserted on the final tables.
- I used **Airflow** to orchestrate and execute multiple interdependent tasks on fixed hour, seeking to know when and how any of them could come to fail.
- I used **GitHub** to host my project for everyone's visibility and accessibility.
- I used **GitHub Actions** in order to ensure that my code will run with no typos and/or integration errors, therefore bringing CI/CD (Continuous Integration and Continuous Deployment) to the project.
- I used **.env**, **GitHub Secrets** and **AWS Secrets Manager** in order to ensure credentials security.
- I used **AWS** and its tools of **RDS, ECS/Fargate, ECR, IAM**, among others in order to deploy and keep my database on the cloud, guaranteeing that the project could work remotely (Hybrid Architecture).
- I used **Google Gemini** as an auxiliary tool for debugging and code optimization. I also used it in order to understand the many different uses and applications of the chosen tools.

# Log and Development Process

Days before: I planned, studied and tried to understand how the architecture of a project works as a whole (macro vision).

Day 31/12: I planned and worked on Scrapy. I was also introduced to WSL2.

### System Architecture Diagram

![architecture-2026-01-25-1726](imgs/1-architecture-2026-01-25-1726.png)

Day 1: I planned and worked on scrapy, ~~integrated Playwright on the program~~ and also integrated WSL2 on VS Code.

Day 2: I planned, instalaled Docker, moved my project to \\wsl$ and remapped the GitHub repository to the new project root folder.

Day 3: I planned, installed a virtual environment to avoid "dependency hell" and also installed Dev Containers for my extensions.

Day 4: I worked to integrate all of the core infrastructure (Windows, WSL2, VS Code, ~~.venv~~, Docker, GitHub and PostgreSQL).

Day 5: Finished integrating the core infrastructure, fixing bugs and mapping errors on the GitHub repository.

Day 6: Integrated the scraper and Dbeaver with Docker's PostgreSQL.

![dbeaver-database-vscode](imgs/2-dbeaver-database-vscode.png)

Day 7: Organized, tested and fixed bugs on the scraper.

Day 8: Planned, updated and tested the scraper. I also installed the dbt and Great Expectations libraries.

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

Day 18: I planned and ran into permission errors on Azure due to my university account; couldn't create a normal account.

Day 19: I planned, explored AWS and began preparations to deploy the project to the cloud.

Day 20: I created the whole cloud infrastructure and deploy my scraper to the AWS ECR. I also integrated Airflow with AWS.

Day 21: Created a PostgreSQL database on the cloud and fixed key and passwords mapping.

Day 22: Fixed the main bugs, permission errors, etc. effectively concluding the pipeline and the main project.

![aws-rds-services](imgs/8-aws-rds-services.png)

Day 23: Fixed silent bugs and decided to make Scrapy run locally in order to avoid private proxies.

Day 24: Scaled the scraper, changing code to scrape 5 items and also added new scrapers for more websites.

Day 25: Gathered information to work on the ReadMe.md file and ensure a good project presentation.

Day 26: Ran into "anti-bot" errors in multiple websites on scrapy; updated my ReadMe.md and gathered images for visualizations.

Day 27: Finished coding my ReadMe.md, concluding the project presentation.

Day 28: Ensured the exclusion of duplicated items on dbt, though I also eased data collection for "price over time".

Day 29: Upgraded GX to warn me on Discord whenever there is a small error, instead of stopping the whole pipeline.

Day 31: Changed my Airflow port from "8080:8080" to "8081:8080" due to browser endless-loading errors.

Extra: Internationalized my ReadMe.md, translating the file from portuguese to english.

![pipeline-final-2026-01-27-0122](imgs/9-pipeline-final-2026-01-27-0122.png)

# Key Takes

Learned to develop an end-to-end data pipeline using industry-standard tools to solve each parts of the system. Some tools I already knew about (Python, SQL, PostgreSQL), but most of them were new to me. Even though, I managed to develop my ideas well, thanks to the many resources I searched for. Among the many key takes I had, here are some of the main ones, indispensable for future events:

- Learned many templates for files like Dockerfile, docker-compose.yml, main.yml, DAG.py, etc.
- Learned to not force a certain version's template of a tool on another version.
- To focus on project security, architecture and infrastructure first and then on the tools' syntax.
- Learned how a whole pipeline cycle works, the data extraction process (API Endpoint/Scrapy/other possible tools), modelling (dbt), quality (GX), storage (PostgreSQL/RDS), orchestration (Airflow), etc.
- Always begin a project adding the .env file if necessary. Don't wait for later.
- Don't worry about "brands", but about project delivery. When Azure rejected me (3 times), I let myself be sent to competition in order to ensure progress.
- When creating a database on AWS, only a single instance will be created. Its name will be postgres, regardless of the other chosen name. In order to fix that, go on DBeaver (or whatever visualization tool you're using), connect to the cloud instance and create a database with a name of your choice.
- In the end, I chose to pull my scraper back to the local environment, for otherwise I would have to pay for private proxies in order to do scraping. Airflow also stood on my local machine, seeing that it would have been unecessarily expensive to have such a demanding and heavy tool running on cloud.

# Credits and References

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

- Python Tutorial Project: https://github.com/lucasrangelt/PYTHONproject
- SQL Tutorial Project: https://github.com/lucasrangelt/SQLcourse
- Diagram Platform: https://excalidraw.com/
- Installing Docker: https://www.youtube.com/watch?time_continue=1599&v=lP8xXebHmuE&embeds_referring_euri=https%3A%2F%2Fgemini.google.com%2F&embeds_referring_origin=https%3A%2F%2Fgemini.google.com&source_ve_path=Mjg2NjY
- Airflow/AWS Tutorial: https://www.youtube.com/watch?v=o88LNQDH2uI
- Tutorial to Install Airflow on Docker: https://www.youtube.com/watch?v=ma8OuIz-ai0
- Airflow 3.1.5 (Documentation): https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
- For references and debug: https://www.startdataengineering.com/
- IBM Data Engineering Course: https://www.coursera.org/professional-certificates/ibm-data-engineer
---
---
---
### Gemini Links

- Tactical Executions: https://gemini.google.com/share/9b04f1af5a43
- Implement the things you need to learn: https://gemini.google.com/share/860923366ed0
- What is each thing: https://gemini.google.com/share/68a31589e27b
- Dbt Source YAML Comparison: https://gemini.google.com/share/1272ec020734
- Data Engineering and Web Scraping Frequency: https://gemini.google.com/share/4834319f82fd

### AI Use Disclosure

In this project, I learned on practice what it meant to use artificial intelligence as a developing tool. Despite AI helping with many suggestions, if they are not ideal and the developer accepts them and goes deep into them, he might lose control of the "steering wheel".

AI is like that old war veteran that, due to age, might end up "exaggerating" or "changing some things from their respective space-time". For instance, he might start talking about how "Eastern Germany is such a backwards country that goes against democracy and its citizens' freedom", and then you remind him that Germany has unified over 30 years ago only to be met with a "Oh, you are absolutely right!!" followed by him agreeing and talking about other things. He has a lot to teach, but if you want to listen to him, you need either a bit of base knowledge or a safe place to test his suppositions/suggestions, lest you fall victim to a code or integration that simply doesn't work, has vulnerabilities or is too outdated.

Most of the time when the AI "hallucinated", was in relation to user interfaces (UI), like DBeaver. Which makes sense, since it's easier for it to work with text and logic elements than with buttons on a screen that it cannot see. Some time, when it came to eliminating the "master" branch that was automatically created by Docker, the AI suggested me a code that looked right at first, but pulled my project back well over a week of progress. Of course, I realized it was dangerous before executing the command and made a backup just in case. No final damage occurred. Good judgement is vital to work with AI.

If the AI doesn't "give you the answer you want", it's practically 100% the way you word it. If you forget something or leave it too vague, the answer might come under-detailed. This is bad for specific/niche problems, but good for those wanting initial suggestions. If you exaggerate on the details, you might get an answer for 5 or 6 kinds of problems when you can barely access one of them. Working with AI taught me optimized ways of formulating questions in order to solve problems.

Let's remember that, despite the many good suggestions I received, in the end I took control and filtered out the ones not to my liking. Here are some of these suggestions (they will probably also be found somewhere within the "Tactical Executions" conversation):

- AI suggested that I use BeautifulSoup. After making a comparison, I chose Scrapy due to scalability and performance.
- AI suggested that I do scraping of only one site, but I built other scrapers to assure scalability.
- AI suggested that my "docker-compose.yml" be put inside the .devcontainers. I followed it, but pulled it to root later.
- AI suggested that I hardcode my credentials (a classic). I used .env due to security risks.
- AI suggested Airflow 2.7.1. I chose Airflow 3.1.5 for being more up to date.
- AI suggested outdated syntax to import GX dependencies. I verified the documentation and updated my code.
- I decided to deleta and rebuild all of my images and volumes (save for my Postgres database) in order to check if it still worked.
- AI suggested that I follow Scrapy >>> dbt >>> GX on Airflow. I chose Scrapy >>> dbt (stg table) >>> GX >>> dbt (end table) for filtering data before loading.
- AI suggested that I use the term "prod" on Github Actions. I preferred to use target "ci" for sounding more appropriate.
- AI suggested naming env variables like "DB_USER". I chose "ENV_USER" for its relation to related env code.
- AI suggested me a bash command to install AWS CLI on my app container. I chose to install it on the Dockerfile.
- AI suggested restricting access to publish on AWS exclusively to my "main" branch. I allowed all of them in order to test possibilities.

**My e-mail: lucasrangel2011@gmail.com**

**My LinkedIn: https://www.linkedin.com/in/lucas-rangel-tietbohl-29791237b/**