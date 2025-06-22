FROM python:3.12-slim

ENV PYTHONBUFFERED=1  
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /code

RUN apt-get update && \
    apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock /code/

RUN poetry install

COPY . /code/

CMD [ "poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]

