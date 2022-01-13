from requests import get

ip = get('https://api.ipify.org').text
print(f'My public IP address is: {ip}')

import ipinfo

access_token = '8dc13cdf266138'
handler = ipinfo.getHandlerAsync(access_token)
ip_address = ip
details = handler.getDetails()

