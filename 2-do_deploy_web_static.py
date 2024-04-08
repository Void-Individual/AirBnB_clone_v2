#!/usr/bin/python3
"""Fabric script to distribute an archive to a web server"""

from fabric.api import run, env, put
from os.path import exists

env.user = "ubuntu"
env.hosts = ['52.91.151.166', '35.174.211.254']


def do_deploy(archive_path):
    """A function to distribute an archive to a remote server"""

    if not exists(archive_path):
        return False

    try:
        # Upload the archive to tmp
        put(archive_path, '/tmp/')

        # Extract the archive
        # Retieve the name of the file in the archive directory
        filename = archive_path.split('/')[-1]
        # Retrieve the name of the file without its extension
        foldername = filename.split('.')[0]
        # Create the location to extract it to if it doesn't exist
        run('mkdir -p /data/web_static/releases/{}'.format(foldername))
        # Extract the compressed file to the desired location
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
            filename, foldername))
        # Delete the transferred archive
        run('rm -rf /tmp/{}'.format(filename))
        # Move the extracted files to the newfolder created
        run(f'mv /data/web_static/releases/{foldername}/web_static/*\
            /data/web_static/releases/{foldername}/')
        # Delete the now empty folder
        run('rm -rf /data/web_static/releases/{foldername}/web_static/')
        # Delete the current symlink
        run('rm -rf /data/web_static/current')
        # Create a new one to the desired location
        run(f'ln -s /data/web_static/releases/{foldername}'
            ' /data/web_static/current')
        print("New version deployed!")

        return True

    except:
        return False
