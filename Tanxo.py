from random import choice
botning_tanlovi = ['Tosh', 'Qaychi', 'Qogoz']
bot = choice(botning_tanlovi)
choise = input(f'Bot {botning_tanlovi} dan birini uyladi\nUshani toping: ')
if choise.tittle() in botning_tanlovi:
    if bot == botning_tanlovi[0]:
        if choise == botning_tanlovi[0]:
            print('durang')
        elif choise == botning_tanlovi[1]:
            print('yutqazdiz')
        else:
            print('yutdiz')
    elif bot == botning_tanlovi[1]:
        if choise == botning_tanlovi[0]:
            print('yutdiz')
        elif choise == botning_tanlovi[1]:
            print('Durrang')
        else:
            print('Yutqzdingiz')
    elif bot == botning_tanlovi[2]:
        if choise == botning_tanlovi[0]:
            print('Yutqzdiz')
        elif choise == botning_tanlovi[1]:
            print('Yutdingiz')
        else:
            print('Durrang')
else:
    print('yoq')
