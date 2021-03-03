#! /bin/sh
INSTANCE_HOME="/app"
CONFIG_FILE="/app/etc/zope.conf"
ZOPE_RUN="/app/bin/runzope"
export INSTANCE_HOME

python create_zope_conf.py "$CONFIG_FILE"
exec "$ZOPE_RUN" -C "$CONFIG_FILE" "$@"