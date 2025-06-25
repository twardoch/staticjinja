#!/usr/bin/env python


import os

import staticjinja

if __name__ == "__main__":
    searchpath = os.path.join(os.getcwd(), "templates")
    site = staticjinja.make_site(searchpath=searchpath)
    site.render(use_reloader=True)
