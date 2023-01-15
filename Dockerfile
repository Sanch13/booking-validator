FROM python:3.11.0-slim

ENV PATH="/opt/poetry/bin:$PATH"

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    curl -sSL https://install.python-poetry.org |  \
    POETRY_HOME=/opt/poetry POETRY_VERSION=1.3.1 python3 - && \
    rm -rf /var/cache/apt

WORKDIR ./app

COPY . .

RUN poetry config virtualenvs.create false && poetry install --no-root

CMD ["python3", "run_bot.py" ]