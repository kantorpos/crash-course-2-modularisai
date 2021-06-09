from urllib import response

import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print('Success !', response)
        print('Content ', response.text)
    else:
        print('Woops, ada kesalahan request', response.status_code)
except Exception as e:
    print('There is an error', e)
print('Program ended !')
