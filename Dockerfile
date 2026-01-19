FROM mcr.microsoft.com/devcontainers/python:3.11
# USER root
RUN apt-get update && apt-get install -y curl \
    libpq-dev \
    gcc \
	postgresql-client \
    # && curl -sL https://aka.ms/InstallAzureCLIDeb | bash \
    && rm -rf /var/lib/apt/lists/*
# USER vscode