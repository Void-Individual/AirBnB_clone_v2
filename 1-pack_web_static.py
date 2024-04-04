#!/usr/bin/python3
"""Module to compile webstatic folder"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """A function to compile an entire folder into an archive"""

    """Using the fabric module to create this dir"""
    local("mkdir -p versions")

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{time}.tgz"

    """Compress the web_static into the tgz file"""
    result = local(f"tar -czvf versions/{archive_name} web_static")

    if result.failed:
        return None
    else:
        return "versions/{}".format(archive_name)
