from z3c.autoinclude.plugin import PluginFinder

ZCML_FILENAMES = ['meta.zcml', 'configure.zcml', 'overrides.zcml']


def main():
    plugin_finder = PluginFinder('plone')
    info = plugin_finder.includableInfo(
        ZCML_FILENAMES)

    for zcml_filename in ZCML_FILENAMES:
        for package in info[zcml_filename]:
            if zcml_filename == 'overrides.zcml':
                print('<includeOverrides package="{}" file="{}" />'.format(
                    package, zcml_filename))
            else:
                print('<include package="{}" file="{}" />'.format(
                    package, zcml_filename))


if __name__ == '__main__':
    main()
