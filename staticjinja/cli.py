#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""staticjinja

Usage:
  staticjinja build [--srcpath=<srcpath> --outpath=<outpath> --static=<a,b,c> \
      --srcmask='*.html']
  staticjinja watch [--srcpath=<srcpath> --outpath=<outpath> --static=<a,b,c> \
      --srcmask='*.html']
  staticjinja (-h | --help)
  staticjinja --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from __future__ import print_function
from docopt import docopt
import os
import staticjinja
import sys


def render(args):
    """
    Render a site.

    :param args:
        A map from command-line options to their values. For example:

            {
                '--help': False,
                '--outpath': None,
                '--srcpath': None,
                '--static': None,
                '--srcmask': None,
                '--version': False,
                'build': True,
                'watch': False
            }
    """
    srcpath = (
        os.path.join(os.getcwd(), 'templates') if args['--srcpath'] is None
        else args['--srcpath'] if os.path.isabs(args['--srcpath'])
        else os.path.join(os.getcwd(), args['--srcpath'])
    )

    if not os.path.isdir(srcpath):
        print("The templates directory '%s' is invalid."
              % srcpath)
        sys.exit(1)

    if args['--outpath'] is not None:
        outpath = args['--outpath']
    else:
        outpath = os.getcwd()

    if not os.path.isdir(outpath):
        print("The output directory '%s' is invalid."
              % outpath)
        sys.exit(1)

    staticdirs = args['--static']
    staticpaths = None

    if staticdirs:
        staticpaths = staticdirs.split(",")
        for path in staticpaths:
            path = os.path.join(srcpath, path)
            if not os.path.isdir(path):
                print("The static files directory '%s' is invalid." % path)
                sys.exit(1)

    srcmask = args.get('--srcmask', None)

    site = staticjinja.make_site(
        searchpath=srcpath,
        outpath=outpath,
        staticpaths=staticpaths,
        searchmask=srcmask
    )

    use_reloader = args['watch']

    site.render(use_reloader=use_reloader)


def main():
    render(docopt(__doc__, version='staticjinja 0.3.0'))


if __name__ == '__main__':
    main()
