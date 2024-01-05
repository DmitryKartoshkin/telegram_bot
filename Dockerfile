FROM python:3.10 as build

WORKDIR app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install --upgrade pip  \
    && pip install -r requirements.txt  \
    && rm -f /var/lib/apt/lists/*

#FROM build

COPY . .
