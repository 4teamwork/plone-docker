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
