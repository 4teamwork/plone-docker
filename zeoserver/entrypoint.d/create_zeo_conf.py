# Create a ZEO configuration file (zeo.conf) from environment variables

import os
import sys


def parse_filestorage_options(value):
    res = {}
    filestorages = value.split(';')
    for filestorage in filestorages:
        storage_options = filestorage.split(',')
        if storage_options:
            storage_name = storage_options[0]
            kwargs = dict([kwarg.split('=') for kwarg in storage_options[1:]])
            res[storage_name] = {
                k.replace('-', '_'): v for k, v in kwargs.items()}
    return res


def main():
    if len(sys.argv) < 2:
        sys.exit("Location for ZEO configuration file required.")
    zeo_conf_file = sys.argv[1]

    env = os.environ
    filestorages = FILESTORAGE_TEMPLATE.format(
        name='1',
        path='/data/filestorage/Data.fs',
        blob_dir='/data/blobstorage',
    )
    additional_filestorages = env.get('FILESTORAGES')
    if additional_filestorages:
        for storage_name, _ in parse_filestorage_options(
            additional_filestorages
        ).items():
            storage_options = {
                'name': storage_name,
                'path': '/data/filestorage/{}.fs'.format(storage_name),
                'blob_dir': '/data/blobstorage-{}'.format(storage_name),
            }
            filestorages += '\n'
            filestorages += FILESTORAGE_TEMPLATE.format(**storage_options)

    zeo_conf = ZEO_CONF_TEMPLATE.format(
        filestorages=filestorages)

    with open(zeo_conf_file, 'w') as file_:
        file_.write(zeo_conf)


ZEO_CONF_TEMPLATE = """\
<zeo>
  address 8100
</zeo>

<eventlog>
  <logfile>
    path STDERR
    format %(asctime)s %(message)s
  </logfile>
</eventlog>

{filestorages}
"""

FILESTORAGE_TEMPLATE = """\
<filestorage {name}>
  path {path}
  blob-dir {blob_dir}
</filestorage>
"""

if __name__ == "__main__":
    main()
