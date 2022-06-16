import os
import requests
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def get_short_link(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    data = {
        "long_url": url,
        "domain": "bit.ly"
    }
    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten',
        headers=headers,
        json=data
    )
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, bitlink):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    params = (
        ('unit', 'month'),
        ('units', '-1'),
        ('unit_reference', '2022-06-08T15:04:05-0700'),
    )

    parsed_url = urlparse(bitlink)
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.netloc}{parsed_url.path}/clicks',
        headers=headers,
        params=params)
    response.raise_for_status()

    number_clicks = response.json()['link_clicks']

    return number_clicks[0]['clicks']


def is_bitlink(token, bitlink):
    headers = {
        'Authorization': f'Bearer {token}',
    }

    parsed_url = urlparse(bitlink)
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.netloc}{parsed_url.path}',
        headers=headers)
    return response.ok


def main():
    parser = argparse.ArgumentParser(
        description="Скрипт возвращает короткую ссылку в сервисе bitly.\
        Если передаваемая ссылка уже короткая, то отображается количество переходов по ней.")
    parser.add_argument("url", help="Ссылка")
    args = parser.parse_args()

    if not is_bitlink(TOKEN, args.url):
        print('Your short link:', get_short_link(TOKEN, args.url))
    else:
        print('Click counts for bitlink:', count_clicks(TOKEN, args.url))

if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.environ['BITLY_API_TOKEN']
    main()
