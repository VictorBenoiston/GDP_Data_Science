from time import sleep


def intinput(text):
    while True:
        number = str(input(text))
        if number.strip() == '' or number.isalpha():
            print('Invalid integer number, try again.')
        else:
            return int(number)
            break


def fileselection():
    command = str(input('Do you want to load a previous file, or create a new one?[open/create]: ')).strip().upper()[0]
    if command in 'C':
        file_name = str(input('Type the file name. Hint: use .txt at the end: '))
        with open(file_name, 'at+') as file_manager:
            print(f'{file_name} successfully created!')
        return file_name
    if command in 'O':
        try:
            existent_file = str(input('Type the file name: '))
            with open(existent_file, 'rt') as file_manager:
                print(f'{existent_file} successfully loaded!')
        except FileNotFoundError:
            print(f'This file was not found. Try again.')
        else:
            return existent_file


def addcountry(file):
    with open(file, 'at') as file_manager:
        while True:
            name = str(input('Type the country name: ')).title()
            name_validation = name.replace(' ', '')
            if not name_validation.isalpha():
                print('Invalid name! Try again')
            else:
                break
        gdp = intinput('Type the country GDP in U$ billions with no comma: U$')
        population = intinput('Type the country population in millions with no comma: ')
        file_manager.write(f'{name};{gdp};{population}\n')
        print(f'Adding {name}...')
        sleep(1)
        print(f'{name} has been successfully added!')
        sleep(1)


def countriesgdp(file):
    print('Loading table...')
    sleep(1)
    with open(file, 'rt') as file_manager:
        for c, lines in enumerate(file_manager):
            data = lines.split(';')
            if c == 0:
                data[1] = str(data[1]).replace('\n', '')
                country_name = 'COUNTRY NAME'
                gdp = 'GDP'
                print('-' * 40)
                print(f'{country_name:<20} {gdp:<14}')
                print('-' * 40)
                print(f'{data[0]:<20} U${data[1]:<8} Bi.')
            else:
                data[1] = str(data[1]).replace('\n', '')
                print(f'{data[0]:<20} U${data[1]:<8} Bi.')
