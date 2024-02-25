# Define the SSH client configuration file path
$ssh_config_file = '/etc/ssh/ssh_config'

# Ensure SSH client configuration file includes the line to use the private key
file_line { 'Declare identity file':
  path   => $ssh_config_file,
  line   => '    IdentityFile ~/.ssh/school',
  ensure => present,
}

# Ensure SSH client configuration file includes the line to refuse password authentication
file_line { 'Turn off passwd auth':
  path   => $ssh_config_file,
  line   => '    PasswordAuthentication no',
  ensure => present,
}
