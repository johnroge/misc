import requests
import bs4


def main():
    print_the_header()

    code = int(input('Enter zip code: '))
    html = get_html_from_web(code)
    get_weather_from_html(html)
    # display the forecast


def print_the_header():
    print('----------------------------------------------')
    print('                Weather App')
    print('----------------------------------------------')
    print()


def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather/us/wa/woodinville/{}'.format(zipcode)
    response = requests.get(url)

    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')


if __name__ == '__main__':
    main()
