import pywapi

CITIES = {
    1: {'name': 'Moscow, Russia', 'code': 'RSXX0063'},
    2: {'name': 'Saint-Petersburg, Russia', 'code': 'RSXX0091'},
    3: {'name': 'New York, USA', 'code': 'USNY0996'},
    4: {'name': 'Los Angeles, USA', 'code': 'USCA0638'},
    5: {'name': 'Washington, USA', 'code': 'USDC0001'},
    6: {'name': 'Ohio, USA','code': 'USIL0884'},
    7: {'name': 'Miami, USA','code': 'USFL0316'},
    8: {'name': 'London, UK', 'code': 'UKXX0085'},
    9: {'name': 'Bristol, UK', 'code': 'UKXX0025'},
    10: {'name': 'Manchester, UK, ', 'code': 'USCA0663'},
    11: {'name': 'Liverpool, UK', 'code': 'USIL0678'},
    12: {'name': 'Wales, UK', 'code': 'UKXX0030'},
    13: {'name': 'Sheffield, UK', 'code': 'UKXX0133'},
    14: {'name': 'Newcastle upon Tyne, UK', 'code': 'UKXX1695'},
    15: {'name': 'Dublin, Ireland','code': 'EIXX0014'},
    16: {'name': 'Toronto, Canada','code': 'CAXX0504'},
    17: {'name': 'Minsk, Belarus','code': 'BOXX0014'},
    18: {'name': 'Grodno, Belarus','code': 'BOMI0841'},
    19: {'name': 'Vitebsk, Belarus','code': 'BOXX0014'},
    20: {'name': 'Mogilev, Belarus','code,': 'BOXX0018'},
    21: {'name': 'Brest, Belarus','code': 'BOXX0023'},
    22: {'name': 'Grodno, Belarus','code': 'BOXX0016'},
    23: {'name': 'Kiev, Ukraine', 'code': 'UPXX0486'},
    24: {'name': 'Jerusalem, Israel', 'code': 'ISXX0010'},
    25: {'name': 'Warsaw, Poland', 'code': 'PLXX0028'},
    26: {'name': 'Melbourne, Australia', 'code': 'ASXX0075'}
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
