FROM python:3.12.2-slim

RUN apt-get update && apt-get install -y libpq-dev

WORKDIR /app

COPY pyproject.toml /app/

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --without dev --no-root

COPY . /app/

EXPOSE 8555

CMD ["task","run"]
