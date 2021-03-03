#! /bin/sh
INSTANCE_HOME="/app"
CONFIG_FILE="/app/etc/zeo.conf"
ZEO_RUN="/app/bin/runzeo"
export INSTANCE_HOME

[[ -d "/data/filestorage" ]] || mkdir /data/filestorage
exec "$ZEO_RUN" -C "$CONFIG_FILE" "$@"