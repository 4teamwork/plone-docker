#! /bin/sh
INSTANCE_HOME="/plone"
CONFIG_FILE="/plone/etc/zeo.conf"
ZEO_RUN="/plone/bin/runzeo"
export INSTANCE_HOME

exec "$ZEO_RUN" -C "$CONFIG_FILE" "$@"