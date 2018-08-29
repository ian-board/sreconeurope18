from geolite2 import geolite2

with open('/tmp/ip.txt') as f:
    reader = geolite2.reader()
    for line in f:
        print(reader.get(line.strip()).get('location').get('longitude'), end=' '),
        print(reader.get(line.strip()).get('location').get('latitude'))
