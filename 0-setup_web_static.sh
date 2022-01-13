#!/usr/bin/env bash
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data
chgrp -R ubuntu /data
