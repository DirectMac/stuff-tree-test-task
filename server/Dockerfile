FROM python:3.10

WORKDIR /app/server
COPY . /app/server
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev
