# Puppet manifest to configure SSH client

# Ensure SSH directory exists
file { '/home/vagrant/.ssh':
  ensure => directory,
  mode   => '0700',
  owner  => 'vagrant',
  group  => 'vagrant',
}

# Copy private key to SSH directory
file { '/home/vagrant/.ssh/school':
  ensure => present,
  source => 'puppet:///modules/ssh/school',
  mode   => '0600',
  owner  => 'vagrant',
  group  => 'vagrant',
}

# Ensure SSH client configuration file exists
file { '/home/vagrant/.ssh/config':
  ensure  => present,
  mode    => '0600',
  owner   => 'vagrant',
  group   => 'vagrant',
  content => "
    Host example-server
      HostName example.com
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
