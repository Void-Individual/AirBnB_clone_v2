#!/usr/bin/python3
"""Scriot to run do pack and do deploy together"""

from fabric.api import local, run
do_pack = __import__('1-pack_web_static.py').do_pack
do_deploy = __import__('2-do_deploy_web_static.py').do_deploy


def deploy():
    """A function that calls the do_pack function and redirects its
    output to the do_deploy function"""

    archive = do_pack()
    if archive:
        status = do_deploy(archive)
    else:
        return False

    return status
