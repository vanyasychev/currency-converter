import json
import requests


class CurrencyConverter:
    def __init__(self, first_code):
        self.first_code = first_code
        self.exchange_rates = dict()

    def data_collection(self):
        return requests.get(f'https://www.floatrates.com/daily/{self.first_code}.json')

    def saving_courses(self):
        courses = ['usd', 'eur']

        if self.first_code in courses:
            courses.remove(self.first_code)

        for i in courses:
            self.exchange_rates[i] = json.loads(self.data_collection().text)[i]['rate']

    def getting_a_course(self, second_code):
        self.exchange_rates[second_code] = json.loads(self.data_collection().text)[second_code]['rate']


def main():
    first_code = input().lower()
    c = CurrencyConverter(first_code)
    c.saving_courses()

    while True:
        second_code = input().lower()
        if not second_code:
            break

        amount = int(input())

        print('Checking the cache...')
        if second_code in c.exchange_rates:
            print('Oh! It is in the cache!')
        else:
            print('Sorry, but it is not in the cache!')
            c.getting_a_course(second_code)

        print(f'You received {round(amount * c.exchange_rates[second_code], 2)} {second_code.upper()}.')


if __name__ == '__main__':
    main()
