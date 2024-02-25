# Puppet manifest to configure SSH client

# Install ssh client package
package { 'openssh-client':
  ensure => installed,
}

# Ensure SSH directory exists
file { '/home/vagrant/.ssh':
  ensure => directory,
  mode   => '0700',
  owner  => 'user',
  group  => 'user',
}

# Copy private key to SSH directory
file { '/home/vagrant/.ssh/school':
  ensure => present,
  source => 'puppet:///modules/ssh/school',
  mode   => '0600',
  owner  => 'user',
  group  => 'user',
}

# Configure SSH client to use private key and refuse password authentication
file { '/home/vagrant/.ssh/config':
  ensure  => present,
  content => "Host server\n  Hostname example.com\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
  mode    => '0600',
  owner   => 'user',
  group   => 'user',
}
