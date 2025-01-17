#! /bin/sh
INSTANCE_HOME="/app"
CONFIG_FILE="/app/etc/zeo.conf"
ZEO_RUN="/app/bin/runzeo"
export INSTANCE_HOME

python create_zeo_conf.py "$CONFIG_FILE"

[[ -d "/data/filestorage" ]] || mkdir /data/filestorage
exec "$ZEO_RUN" -C "$CONFIG_FILE" "$@"