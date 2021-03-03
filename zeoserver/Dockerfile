FROM python:2.7-alpine as build-stage

RUN addgroup -S -g 800 plone \
 && adduser -S -D -G plone -u 800 plone

RUN mkdir -p /plone

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    libc-dev \
    zlib-dev

WORKDIR /plone

RUN pip install virtualenv && virtualenv .
COPY versions.txt ./
RUN /plone/bin/pip install --no-cache-dir ZODB3 -c versions.txt

RUN mkdir -p /data/filestorage /data/blobstorage /plone/var
RUN chown -R plone:plone /data /plone/var
COPY etc /plone/etc


FROM python:2.7-alpine

RUN addgroup -S -g 800 plone \
 && adduser -S -D -G plone -u 800 plone

COPY --from=build-stage /plone /plone

RUN mkdir -p /data/filestorage /data/blobstorage
# Currently ownership and permissions are not preserved when copying from
# another stage. Should be fixed with Docker 19.03 or later 
# https://github.com/moby/moby/pull/38599
RUN chown -R plone:plone /data /plone/var

VOLUME /data

USER plone
EXPOSE 8100
WORKDIR /plone

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
