FROM python:3.7
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

WORKDIR /src

RUN apt-get update && apt-get install -y postgresql-client
COPY requirements.txt /src
RUN pip install -r requirements.txt

COPY image_parroter /src/image_parroter
COPY thumbnailer /src/thumbnailer
COPY manage.py /src
COPY *.sh /src/

CMD python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000