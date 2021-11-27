FROM alpine:3.14 as build-stage

RUN addgroup -S -g 800 plone \
 && adduser -S -D -G plone -u 800 plone

RUN mkdir -p /app

RUN --mount=type=cache,target=/var/cache/apk apk add --virtual .build-deps \
    gcc \
    libc-dev \
    zlib-dev \
    python2-dev \
    py2-setuptools

WORKDIR /app

RUN wget https://bootstrap.pypa.io/virtualenv/2.7/virtualenv.pyz \
 && python virtualenv.pyz . \
 && rm virtualenv.pyz

ENV VIRTUAL_ENV=/app
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY versions.txt ./

RUN --mount=type=cache,target=/root/.cache pip install ZODB3 -c versions.txt

RUN mkdir -p /app/var
RUN chown -R plone:plone /app/var
COPY etc /app/etc
COPY docker-entrypoint.sh /app/

FROM alpine:3.14

RUN addgroup -S -g 800 plone \
 && adduser -S -D -G plone -u 800 plone

RUN --mount=type=cache,target=/var/cache/apk apk add \
    python2

COPY --from=build-stage /app /app

RUN mkdir -p /data \
 && chown -R plone:plone /data

VOLUME /data
USER plone
EXPOSE 8100
WORKDIR /app

ENTRYPOINT ["/app/docker-entrypoint.sh"]
