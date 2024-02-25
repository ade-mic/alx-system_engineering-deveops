# make changes to SSH  configuration file
file_line { 'change identity_file':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => 'IdentifyFile ~/.ssh/school',
}

file_line { 'ssh passwordauth':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => 'PasswordAuthentication no',
match  => '^#?PasswordAuthentication',
}