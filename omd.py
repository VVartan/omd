def step2_umbrella():
    print('☂️+🦆')
def step2_no_umbrella():  
  print('Sorry, wet duck')

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    print('Sorry, wet duck')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if option == 'да':
        return step2_umbrella()
    return step2_no_umbrella()

if __name__ == '__main__':
    step1()
