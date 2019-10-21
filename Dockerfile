FROM python:3.6.9

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

COPY . /app

RUN apt-get update -y \
    && apt-get install -y  locales binutils libproj-dev gdal-bin python-gdal \
    && pip install --no-cache-dir -r /app/requirements/production.txt \
    && groupadd -r django \
    && useradd -r -g django django \
    && echo fr_FR.UTF-8 UTF-8 >> /etc/locale.gen \
    && echo en_US.UTF-8 UTF-8 >> /etc/locale.gen \
    && locale-gen \
    && rm -rf /var/lib/apt/lists/* /tmp/* /app/requirements

RUN chown -R django /app

WORKDIR /app

USER django

ENTRYPOINT ["/app/docker-entrypoint.sh"]
