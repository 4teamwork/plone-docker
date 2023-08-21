FROM 4teamwork/python:2.7 as build-stage

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
    gettext

WORKDIR /app

RUN echo "/app/lib/python2.7/site-packages/" > /usr/local/lib/python2.7/site-packages/app.pth

COPY versions.txt ./

RUN --mount=type=cache,target=/root/.cache pip install --prefix /app Plone Products.PloneHotfix20210518 -c versions.txt


# Fix missing .mo files in p.a.discussion
RUN find /app/lib/python2.7/site-packages/plone/app/discussion/i18n -name "*.po" | xargs -I@ sh -c 'msgfmt @ -o "$(dirname @)/$(basename @ .po)".mo'

COPY docker-entrypoint.sh create_zope_conf.py inituser /app/
RUN mkdir -p /app/var /app/etc \
 && chown -R plone:plone /app/var /app/etc
COPY etc /app/etc


FROM 4teamwork/python:2.7

RUN addgroup -S -g 800 plone \
 && adduser -S -D -G plone -u 800 plone

RUN apk add \
    libxml2 \
    libxslt \
    libjpeg-turbo \
    tzdata

COPY --from=build-stage /app /app
RUN echo "/app/lib/python2.7/site-packages/" > /usr/local/lib/python2.7/site-packages/app.pth \
 && echo "import site; site.addsitedir('/app/lib/python2.7/site-packages')" > /usr/local/lib/python2.7/site-packages/sitecustomize.py

RUN mkdir -p /data/filestorage /data/blobstorage \
 && chown -R plone:plone /data

ENV TZ=Europe/Zurich
VOLUME /data
USER plone
EXPOSE 8080
WORKDIR /app

ENTRYPOINT ["/app/docker-entrypoint.sh"]
