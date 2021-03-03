FROM python:2.7-alpine as build-stage

RUN addgroup -S -g 800 plone \
 && adduser -S -D -G plone -u 800 plone

RUN mkdir -p /app

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    libc-dev \
    zlib-dev

WORKDIR /app

RUN pip install virtualenv \
 && virtualenv .

ENV VIRTUAL_ENV=/app
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY versions.txt ./

RUN pip install --no-cache-dir ZODB3 -c versions.txt

RUN mkdir -p /app/var
RUN chown -R plone:plone /app/var
COPY etc /app/etc
COPY docker-entrypoint.sh /app/

FROM python:2.7-alpine

RUN addgroup -S -g 800 plone \
 && adduser -S -D -G plone -u 800 plone

COPY --from=build-stage /app /app

RUN mkdir -p /data \
 && chown -R plone:plone /data

VOLUME /data
USER plone
EXPOSE 8100
WORKDIR /app

ENTRYPOINT ["/app/docker-entrypoint.sh"]
