FROM mcantillana/django_unab

RUN apk add --no-cache jpeg-dev zlib-dev

ADD requeriments.txt /code
RUN pip install -r requeriments.txt
