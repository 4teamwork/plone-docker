FROM 4teamwork/python:2.7 as build-stage

RUN addgroup -S -g 800 plone \
 && adduser -S -D -G plone -u 800 plone

RUN mkdir -p /app

RUN apk -U upgrade && apk add \
    gcc \
    libc-dev \
    zlib-dev \
    libjpeg-turbo-dev \
    libpng-dev \
    libxml2-dev \
    libxslt-dev \
    gettext \
    curl \
    patch

WORKDIR /app

RUN echo "/app/lib/python2.7/site-packages/" > /usr/local/lib/python2.7/site-packages/app.pth

COPY versions.txt ./

COPY patches /var/tmp/patches

# Install Pillow with security patches
RUN --mount=type=cache,target=/root/.cache \
 curl -o /var/tmp/Pillow-6.2.2.tar.gz https://files.pythonhosted.org/packages/b3/d0/a20d8440b71adfbf133452d4f6e0fe80de2df7c2578c9b498fb812083383/Pillow-6.2.2.tar.gz \
 && cd /var/tmp \
 && tar xzvf Pillow-6.2.2.tar.gz \
 && rm Pillow-6.2.2.tar.gz \
 && cd Pillow-6.2.2 \
 && patch -p 1 -i /var/tmp/patches/CVE-2020-11538.patch \
 && patch -p 1 -i /var/tmp/patches/CVE-2020-35653.patch \
 && patch -p 1 -i /var/tmp/patches/CVE-2020-35655.patch \
 && patch -p 1 -i /var/tmp/patches/CVE-2021-25290.patch \
 && patch -p 1 -i /var/tmp/patches/CVE-2021-25292.patch \
 && patch -p 1 -i /var/tmp/patches/CVE-2021-25293.patch \
 && patch -p 1 -i /var/tmp/patches/CVE-2021-27921_27922_27923.patch \
 && patch -p 1 -i /var/tmp/patches/CVE-2021-25287_25288.patch \
 && patch -p 1 -i /var/tmp/patches/CVE-2021-28675.patch \
 && patch -p 1 -i /var/tmp/patches/CVE-2021-28676.patch \
 && patch -p 1 -i /var/tmp/patches/CVE-2021-28677.patch \
 && patch -p 1 -i /var/tmp/patches/CVE-2021-28678.patch \
 && patch -p 1 -i /var/tmp/patches/CVE-2021-34552.patch \
 && patch -p 1 -i /var/tmp/patches/CVE-2022-22817.patch \
 && patch -p 1 -i /var/tmp/patches/CVE-2022-22815_CVE-2022-22816.patch \
 && patch -p 1 -i /var/tmp/patches/CVE-2023-44271.patch \
 && patch -p 1 -i /var/tmp/patches/CVE-2023-50447.patch \
 && patch -p 1 -i /var/tmp/patches/CVE-2024-28219.patch \
 && pip install /var/tmp/Pillow-6.2.2 --prefix /app

RUN --mount=type=cache,target=/root/.cache pip install --prefix /app Plone Products.PloneHotfix20210518 cssselect -c versions.txt

COPY ./patches/z3c_autoinclude_utils.py /app/lib/python2.7/site-packages/z3c/autoinclude/utils.py
RUN python2.7 -m compileall /app/lib/python2.7/site-packages/z3c/autoinclude/utils.py

# Fix missing .mo files in p.a.discussion
RUN find /app/lib/python2.7/site-packages/plone/app/discussion/i18n -name "*.po" | xargs -I@ sh -c 'msgfmt @ -o "$(dirname @)/$(basename @ .po)".mo'

COPY docker-entrypoint.sh create_zope_conf.py inituser /app/
RUN mkdir -p /app/var /app/etc \
 && chown -R plone:plone /app/var /app/etc
COPY etc /app/etc


FROM 4teamwork/python:2.7

RUN addgroup -S -g 800 plone \
 && adduser -S -D -G plone -u 800 plone

RUN apk update && apk add \
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
