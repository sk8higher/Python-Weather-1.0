import pywapi

CITIES = {
    1: {'name': 'Moscow', 'code': 'RSXX0063'},
    2: {'name': 'Minsk', 'code': 'BOXX0014'},
    3: {'name': 'Saint-Petersburg', 'code': 'RSXX0091'},
    4: {'name': 'New York', 'code': 'USNY0996'},
    5: {'name': 'London', 'code': 'UKXX0085'},
    6: {'name': 'Bristol', 'code': 'UKXX0025'},
    7: {'name': 'Kiev', 'code': 'UPXX0486'},
    8: {'name': 'Los Angeles', 'code': 'USCA0638'},
    9: {'name': 'Jerusalim', 'code': 'ISXX0010'},
    10: {'name': 'Warsaw', 'code': 'PLXX0028'},
}


def get_choose():
    for city_key, city_val in CITIES.items():
        print('{} - {}'.format(city_key, city_val['name']))
    city = int(input('\nChoose your city: '))
    if city in CITIES:
        return CITIES[city]
    else:
        return None


def get_weather(city):
    return pywapi.get_weather_from_weather_com(city['code'])


def print_weather(weather, city):
    weather_current = weather['current_conditions']
    print('Weather.com says: It is {} and {} C now in {}.\n\n'
          .format(weather_current['text'],
                  weather_current['temperature'],
                  city['name']))


if __name__ == '__main__':
    city = get_choose()
    if city:
        weather = get_weather(city)
        print_weather(weather, city)
    else:
        print('Wrong city code')
