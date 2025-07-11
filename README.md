# Plone for Docker

Plone and ZEO images optimized for running in production.

The images are based on Alpine Linux.
Plone is installed using pip.
Configuration options can be provided through environment variables.


## Usage

For a quick start use the provided Docker Compose file. Simply startup Plone
with

```
docker-compose up -d
```

## Configuration

| Environment variable | Default value  |
|----------------------|----------------|
| ZODB_CACHE_SIZE      | 100000         |
| STORAGE              | zeoclient      |
| ZEO_ADDRESS          | zeoserver:8100 |
| ZSERVER_THREADS      | 1              |
| DEBUG_MODE           | off            |
| VERBOSE_SECURITY     | off            |
| READ_ONLY            | false          |

### Additional filestorages

Additional filestorages can be added with the `ADDITIONAL_FILESTORAGES` environment
variable. For each filestorage a name must be provided. Multiple filestorages
are separated by a semicolon. Filestorage options can be given after the filestorage
name and are separated by a comma. 

Example:

```
ADDITIONAL_FILESTORAGES='mystorage,zodb-cache-size=5000;otherstorage,mountpoint=/foo:/bar'
```

## Building multi-platform images

Create a builder instance:

```
docker buildx create --name plonebuilder --use --bootstrap
```

Build images:

```
docker buildx build --platform linux/amd64,linux/arm64 --tag 4teamwork/zeoserver:4.3.20 --tag 4teamwork/zeoserver:4.3.20-alpine3.18 --push ./zeoserver
docker buildx build --platform linux/amd64,linux/arm64 --tag 4teamwork/plone:4.3.20 --tag 4teamwork/plone:4.3.20-alpine3.18 --push ./plone
```
