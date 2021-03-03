FROM python:2.7-alpine AS build-stage

RUN addgroup -S -g 800 plone \
 && adduser -S -D -G plone -u 800 plone

RUN mkdir -p /app

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    libc-dev \
    zlib-dev \
    libjpeg-turbo-dev \
    libpng-dev \
    libxml2-dev \
    libxslt-dev \
    gettext

WORKDIR /app

RUN pip install virtualenv \
 && virtualenv .

ENV VIRTUAL_ENV=/app
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY versions.txt ./

# RUN --mount=type=cache,target=/root/.cache pip install Plone -c versions.txt
RUN pip install --no-cache-dir Plone -c versions.txt

# Fix missing .mo files in p.a.discussion
RUN find /app/lib/python2.7/site-packages/plone/app/discussion/i18n -name "*.po" | xargs -I@ sh -c 'msgfmt @ -o "$(dirname @)/$(basename @ .po)".mo'

COPY docker-entrypoint.sh create_zope_conf.py inituser /app/
RUN mkdir -p /app/var /app/etc \
 && chown -R plone:plone /app/var /app/etc
COPY etc /app/etc


FROM python:2.7-alpine

RUN addgroup -S -g 800 plone \
 && adduser -S -D -G plone -u 800 plone

RUN apk add --no-cache \
    libxml2 \
    libxslt \
    libjpeg-turbo

COPY --from=build-stage /app /app

RUN mkdir -p /data/filestorage /data/blobstorage \
 && chown -R plone:plone /data

VOLUME /data
USER plone
EXPOSE 8080
WORKDIR /app

# CMD ["/bin/sh"]
ENTRYPOINT ["/app/docker-entrypoint.sh"]
