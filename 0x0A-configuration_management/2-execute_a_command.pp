# kill process killmenow task3

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
