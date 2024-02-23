# Using Puppet, install flask from pip3
# Ensure pip3 is installed
package { 'python3-pip':
  ensure => 'installed',
}

# Install Werkzeug version 2.1.1 using pip3
exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install werkzeug==2.1.1',
  path    => ['/usr/bin'],
  unless  => '/usr/bin/pip3 show werkzeug | grep -q "Version: 2.1.1"',
}

# Install Flask version 2.1.0 using pip3
exec { 'install_flask':
  command => 'pip3 install',
  path    => ['/usr/bin'],
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
