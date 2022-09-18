
import geocoder as geo

ip_address = geo.ip('me')
print(ip_address)

ip = geo.ip('192.xxx.xxx.x')
print(ip.city)

print(ip.latlng)


