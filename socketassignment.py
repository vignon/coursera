import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.data.pr4e.org', 80))
s.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

while True:
  data = s.recv(512)
  if len(data) < 1 : break
  str = data.split('\r\n')
  print str[1] #Content Type
  print str[2] #Content Length
  print str[6] #Last Modified
  print str[7] #Etag
  break

s.close()
