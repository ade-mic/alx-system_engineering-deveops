#!/usr/bin/puppet
# Define Nginx installation and configuration
# Ensure apt-get update is performed before installing packages
exec { 'apt_update':
  command => '/usr/bin/apt-get update',
  path    => ['/usr/bin'],
}

# Install Nginx
package { 'nginx':
  ensure => installed,
  require => Exec['apt_update'], # Ensure apt-get update is executed first
}

# Configure Nginx to serve "Hello World!" at the root
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
}

# Configure Nginx to serve a custom 404 page
file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page!\n",
}

# Configure Nginx to listen on port 80 and define server block
file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;

      root /var/www/html;
      index index.html index.htm index.debian.html;

      server_name _;

      location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
      }

      location / {
        try_files \$uri \$uri/ =404;
      }

      error_page 404 /404.html;
    }
  ",
}

# Restart Nginx service whenever the configuration changes
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
