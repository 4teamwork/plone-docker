FROM alpine:3.14 AS build-stage

RUN addgroup -S -g 800 plone \
 && adduser -S -D -G plone -u 800 plone

RUN mkdir -p /app

RUN apk add --virtual .build-deps \
    gcc \
    libc-dev \
    zlib-dev \
    libjpeg-turbo-dev \
    libpng-dev \
    libxml2-dev \
    libxslt-dev \
    python2-dev \
    gettext

WORKDIR /app

RUN wget https://bootstrap.pypa.io/virtualenv/2.7/virtualenv.pyz \
 && python virtualenv.pyz . \
 && rm virtualenv.pyz

ENV VIRTUAL_ENV=/app
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY versions.txt ./

RUN --mount=type=cache,target=/root/.cache pip install Plone Products.PloneHotfix20210518 -c versions.txt

# Fix missing .mo files in p.a.discussion
RUN find /app/lib/python2.7/site-packages/plone/app/discussion/i18n -name "*.po" | xargs -I@ sh -c 'msgfmt @ -o "$(dirname @)/$(basename @ .po)".mo'

COPY docker-entrypoint.sh create_zope_conf.py inituser /app/
RUN mkdir -p /app/var /app/etc \
 && chown -R plone:plone /app/var /app/etc
COPY etc /app/etc


FROM alpine:3.14

RUN addgroup -S -g 800 plone \
 && adduser -S -D -G plone -u 800 plone

RUN apk add \
    libxml2 \
    libxslt \
    libjpeg-turbo \
    tzdata \
    python2

RUN --mount=type=cache,target=/var/cache/apk apk add --virtual .build-deps \
    python2

COPY --from=build-stage /app /app

RUN mkdir -p /data/filestorage /data/blobstorage \
 && chown -R plone:plone /data

ENV TZ=Europe/Zurich
VOLUME /data
USER plone
EXPOSE 8080
WORKDIR /app

ENTRYPOINT ["/app/docker-entrypoint.sh"]
