#!/usr/bin/python


from pisi.actionsapi import get, autotools, pisitools

def install():
    files = ["basket.py", "groups.py", "updates.py",
             "components.py", "interface.py", "package_view.py", "widgets.py"]

    for f in files:
        pisitools.insinto("/usr/lib/solus-sc", f)
    pisitools.dobin("main.py")
    pisitools.domove("/usr/bin/main.py", "/usr/bin", destinationFile="solus-sc")
    pisitools.insinto("/usr/share/applications", "data/solus-sc.desktop")
