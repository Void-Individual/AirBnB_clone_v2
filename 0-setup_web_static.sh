#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static.

# Update previous packages
sudo apt-get update
# Install nginx
sudo apt-get -y install nginx
# Create these folders if they do not exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a test html file
index="<html>
    <head>
        <title>Test Page</title>
    </head>
    <body style='background-color:#788b9b;height:70px;width:100%;'>
        <p>This is a test. Your nginx script works</p>
    </body>
</html>
"
echo "$index" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# If this symlink exists, delete and recreate it everytime
if [ -L "/data/web_static/current" ]; then
    rm /data/web_static/current
fi
# Create the symlink again
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the data folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "/server_name _;/a \\\nlocation /hbnb_static {\n\talias /data/web_static/current/;}" /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx restart
