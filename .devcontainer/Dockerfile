FROM mcr.microsoft.com/devcontainers/python:3.11
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
	postgresql-client \
    && rm -rf /var/lib/apt/lists/*