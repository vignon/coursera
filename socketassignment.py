import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.data.pr4e.org', 80))
s.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

while True:
  data = s.recv(512)
  if len(data) < 1 : break
  str = data.split('\r\n')
  print 'Content Type:', str[1]
  print 'Content Length', str[2]
  print 'Last Modified', str[6]
  print 'Etag', str[7]
  break

s.close()
