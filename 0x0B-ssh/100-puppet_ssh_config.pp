# make changes to SSH  configuration file
file_line { 'ssh_config_keyfile':
  path    => '/home/vagrant/.ssh/config',
  line    => "IdentityFile ~/.ssh/school",
  match   => "IdentityFile <existing_keyfile>",
  ensure  => present,
}
file_line { 'modify_ssh_config':
  path    => '/home/vagrant/.ssh/config'
  line    => 'PasswordAuthentication no',
  match   => '^#?PasswordAuthentication',
  ensure  => present,
}
