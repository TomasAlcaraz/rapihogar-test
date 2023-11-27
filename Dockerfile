# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update \
    && apt-get install -y libpq-dev
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./project /code/

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--blind", ":8000", "--chdir", "rapihogar", "rapihogar.wsgi:application"]
