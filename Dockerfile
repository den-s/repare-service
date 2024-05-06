FROM python:3.9
RUN mkdir /data
WORKDIR /data

ADD ./req.txt /data

# RUN apk add --update --no-cache g++ gcc libxslt-dev postgresql-dev python3-dev musl-dev libxml2-dev
# RUN apk add --update --no-cache jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN pip install -U pip setuptools virtualenv

RUN pip install -r req.txt
ADD . /data

RUN chmod +x ./docker-entrypoint.sh
ENTRYPOINT ./docker-entrypoint.sh

RUN apt-get update && apt-get -y install cron
RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log
