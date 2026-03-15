package { 'docker':
  ensure => installed,
}

service { 'docker':
  ensure => running,
}