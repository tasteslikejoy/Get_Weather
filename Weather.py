import requests
import datetime
from config import weather_token


def get_weather(message, weather_token):

    code_to_smile = {
        'Clear': 'Ясно ☀',
        'Clouds': 'Облачно 🌤',
        'Rain': 'Дождь 🌧',
        'Drizzle': 'Дождь 🌦',
        'Thunderstorm': 'Гроза ⛈',
        'Snow': 'Снег 🌨',
        'Mist': 'Туман 😶‍🌫'
    }

    try :
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message}&appid={weather_token}&units=metric')
        data = r.json()

        message = data['name']
        cur_weather = data['main']['temp']

        weather_description = data['weather'][0]['main']

        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри в окно, не понимаю ничего! Что там происходит⁉⁉⁉'

        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        len_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')

        print (f'***{current_date}***'
              f'\nПогода в городе {message}\nТемпература: {cur_weather}°C {wd}\nВлажность: {humidity}%'
              f'\nСкорость ветра: {wind}м/с.'
              f'\nПрожолжительность светового дня: {len_day}\nРассвет: {sunrise}\nЗакат: {sunset}'
              f'\nХорошего дня!')

    except Exception as ex:
        print(ex)

def  main():
    city = input("Введите ваш город: ")
    get_weather(city, weather_token)

if __name__ == '__main__':
    main()

