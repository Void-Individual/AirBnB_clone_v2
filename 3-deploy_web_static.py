#!/usr/bin/python3
"""Scriot to run do pack and do deploy together"""

from importlib import import_module

pack_module = import_module("1-pack_web_static")
do_pack = pack_module.do_pack

deploy_module = import_module("2-do_deploy_web_static")
do_deploy = deploy_module.do_deploy

# A global variable to store the archive path once
saved_archive = None


def deploy():
    """A function that calls the do_pack function and redirects its
    output to the do_deploy function"""

    # Access the archive
    global saved_archive

    if saved_archive:
        archive = saved_archive
    else:
        archive = do_pack()
        if archive:
            saved_archive = archive
        else:
            return False

    return do_deploy(archive)
