# make changes to SSH  configuration file
file { '/etc/ssh/sshd_config':
ensure => present,
content => "
Host 352442-web-01
    HostName 54.85.90.192
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}