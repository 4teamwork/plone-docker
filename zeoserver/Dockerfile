ARG ALPINE_VERSION=3.22
FROM 4teamwork/python:2.7-alpine${ALPINE_VERSION} AS build-stage

RUN addgroup -S -g 800 plone \
 && adduser -S -D -G plone -u 800 plone

RUN mkdir -p /app

RUN apk add \
    gcc \
    libc-dev \
    zlib-dev

WORKDIR /app

COPY versions.txt ./

RUN echo "/app/lib/python2.7/site-packages/" > /usr/local/lib/python2.7/site-packages/app.pth

RUN --mount=type=cache,target=/root/.cache pip install --prefix /app ZODB3 -c versions.txt

RUN mkdir -p /app/var/log /app/etc \
 && chown -R plone:plone /app/var /app/etc
COPY docker-entrypoint.sh /app/
COPY entrypoint.d /app/entrypoint.d


FROM 4teamwork/python:2.7-alpine${ALPINE_VERSION}

RUN addgroup -S -g 800 plone \
 && adduser -S -D -G plone -u 800 plone

COPY --from=build-stage /app /app
RUN echo "/app/lib/python2.7/site-packages/" > /usr/local/lib/python2.7/site-packages/app.pth \
 && echo "import site; site.addsitedir('/app/lib/python2.7/site-packages')" > /usr/local/lib/python2.7/site-packages/sitecustomize.py

RUN mkdir -p /data \
 && chown -R plone:plone /data

VOLUME /data
USER plone
EXPOSE 8100
WORKDIR /app

ENTRYPOINT ["/app/docker-entrypoint.sh"]
