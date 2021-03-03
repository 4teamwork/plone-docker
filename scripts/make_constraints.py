from zc.buildout.buildout import Buildout
import sys


def get_buildout(version):
    versions_url = 'http://dist.plone.org/release/{version}/versions.cfg'
    url = versions_url.format(version=version)
    buildout = Buildout(
        config_file=url,
        cloptions=[('buildout', 'directory', '/tmp')],
        user_defaults=False,
    )
    return buildout


def get_versions(buildout):
    for version in buildout['versions'].items():
        yield '=='.join(version)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        version = sys.argv[1]
    else:
        version = '5-latest'

    buildout = get_buildout(version)
    print('\n'.join(sorted(get_versions(buildout))))
