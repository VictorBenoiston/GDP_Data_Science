from file_functions import *


def mainmenu(file):
    while True:
        sleep(1)
        print('-' * 40)
        print('Main menu'.center(40))
        print('-' * 40)
        print('1 - Add a new country;\n'
              '2 - Show the countries/GDP table;\n'
              '3 - Show the data science table;\n'
              '4 - Exit.')
        print('-' * 40)
        command = int(input('Your selection: '))
        if command > 4:
            print('Invalid command, try again!')
        if command == 1:
            addcountry(file)
        if command == 2:
            countriesgdp(file)
        if command == 3:
            print('Loading list...')
            sleep(1)
            gdp_total = 0
            with open(file, 'rt') as file_manager:
                country_name = 'COUNTRY NAME'
                gdp = 'GDP'
                population = 'POPULATION'
                print('-' * 45)
                print(f'{country_name:<20} {gdp:<12} {population:<10}')
                print('-' * 45)
                c = 1
                for c, line in enumerate(file_manager):
                    c += 1
                    data = line.split(';')
                    data[2] = str(data[2]).replace('\n', '')
                    gdp_total += int(data[1])
                    data[1] = f'{data[1]} Bi.'
                    print(f'{data[0]:<20} {data[1]:<12} {data[2]} Mi.')
                print('-' * 45)
                total = f'TOTAL: {c}'
                gdp_average = gdp_total / c
                gdp_printable = f'Average: U${gdp_average:,.2f} Mi.'
                print(f'{total:<20} {gdp_printable}')
            sleep(1)
        if command == 4:
            break




