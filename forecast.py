import requests


city = 'Moscow,RU'
appid = '7714dfcaa87c0acb060d44ec8d390570'
res = requests.get('http://api.openweathermap.org/data/2.5/forecast',
                   params={'q': city, 'units': 'metric',
                           'lang': 'ru', 'APPID': appid})
data = res.json()
print("Prognoz pogody na nedelyu:")
for i in data['list']:
    print(f"Data <f{i['dt_txt']}>\r\nTemperatura"
          f"<{'{0:+3.0f}'.format(i['main']['temp'])}>\r\n"
          f"Pogodnye usloviya <{i['weather'][0]['description']}>\r\n"
          f"Vidimost\' <{i['visibility']}>\r\n"
          f"'Napravleniye vetra <{i['wind']['deg']}>")
print('____________________')