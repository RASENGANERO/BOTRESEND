from PIL import Image, ImageDraw, ImageFont
from random import randint

# all phrases
phrases = [
    # Общение
    {
        'text': '"Может\nпойдем?"\n   - Сиди \n    нахуй',
        'font_size': 28,
        'coordinates': [{
            'x': 100,
            'y': 420
        }]
    },  # 1
    {
        'text': '  "Мы это\nвырежем"',
        'font_size': 28,
        'coordinates': [{
            'x': 90,
            'y': 460
        }]
    },  # 2
    {
        'text': '"Я в туалет,\n   можно?"\n  - Сцы тут',
        'font_size': 24,
        'coordinates': [{
            'x': 93,
            'y': 460
        }]
    },  # 3
    {
        'text': 'А можно\n    колу?\n   и лед!',
        'font_size': 28,
        'coordinates': [{
            'x': 100,
            'y': 450
        }]
    },  # 4
    {
        'text': 'Воздержа\n    ние от\nчего-либо\n   N-минут\nбез успеха',
        'font_size': 24,
        'coordinates': [{
            'x': 100,
            'y': 420
        }]
    },  # 5
    {
        'text': '  Всратая\n  реклама\nАвиасейлз',
        'font_size': 25,
        'coordinates': [{
            'x': 90,
            'y': 445
        }]
    },  # 6
    {
        'text': ' Двойничок\n    Смеются\n      только\n2 участника',
        'font_size': 22,
        'coordinates': [{
            'x': 93,
            'y': 435
        }]
    },  # 7
    {
        'text': 'Каламбуры\n  на уровне\nсловесного\n    поноса',
        'font_size': 23,
        'coordinates': [{
            'x': 93,
            'y': 435
        }]
    },  # 8
    {
        'text': 'Кокешки',
        'font_size': 30,
        'coordinates': [{
            'x': 93,
            'y': 470
        }]
    },  # 9
    {
        'text': 'Коллектив\n ное пение\n    в угаре',
        'font_size': 26,
        'coordinates': [{
            'x': 90,
            'y': 445
        }]
    },  # 10
    {
        'text': '          Кто-то\n    оговорился\n     и 20 минут\n это разгоняют',
        'font_size': 19,
        'coordinates': [{
            'x': 85,
            'y': 440
        }]
    },  # 11
    {
        'text': 'Начало тейбла\nчерез 30 минут\n после начала',
        'font_size': 18,
        'coordinates': [{
            'x': 85,
            'y': 460
        }]
    },  # 12
    {
        'text': '  Отслыки\n к другому\n    тейблу',
        'font_size': 28,
        'coordinates': [{
            'x': 84,
            'y': 440
        }]
    },  # 13
    {
        'text': '    Очень\nнеловкая\n    пауза',
        'font_size': 28,
        'coordinates': [{
            'x': 94,
            'y': 435
        }]
    },  # 14
    {
        'text': '  Попытка\nобъяснить\n    смысл\n   тейбла',
        'font_size': 26,
        'coordinates': [{
            'x': 93,
            'y': 430
        }]
    },  # 15
    {
        'text': '     Разгон\nзвуков или\nотдельных\n     слогов',
        'font_size': 24,
        'coordinates': [{
            'x': 93,
            'y': 435
        }]
    },  # 16
    {
        'text': 'Отсылка к\nСамохуну',
        'font_size': 27,
        'coordinates': [{
            'x': 90,
            'y': 455
        }]
    },  # 17
    {
        'text': '       Тема\n"Предметы\n     в жопе"',
        'font_size': 25,
        'coordinates': [{
            'x': 85,
            'y': 445
        }]
    },  # 18
    {
        'text': '          Шутка\n   "ну мы еще\nразгоны сюда\n    приносить\n       должны?"',
        'font_size': 20,
        'coordinates': [{
            'x': 88,
            'y': 430
        }]
    },  # 19
    {
        'text': '          Шутка\n"ты вырыл яму\n          и я-мы\n       нырнули"',
        'font_size': 20,
        'coordinates': [{
            'x': 84,
            'y': 440
        }]
    },  # 20
    {
        'text': '    Шутка\n"У нас тут\n  6 камер"',
        'font_size': 26,
        'coordinates': [{
            'x': 93,
            'y': 445
        }]
    },  # 21
    {
        'text': '      Шутка\n"Я лучше на\nвойну поеду"',
        'font_size': 21,
        'coordinates': [{
            'x': 93,
            'y': 450
        }]
    },  # 22
    {
        'text': '         Шутка\n     "Я лучше\nобратно в РФ"',
        'font_size': 19,
        'coordinates': [{
            'x': 90,
            'y': 455
        }]
    },  # 23
    {
        'text': '   Шутка\nв тишину',
        'font_size': 26,
        'coordinates': [{
            'x': 100,
            'y': 455
        }]
    },  # 24
    {
        'text': ' Шутка\nпро вес\n   Ильи',
        'font_size': 26,
        'coordinates': [{
            'x': 115,
            'y': 445
        }]
    },  # 25
    # Зрители
    {
        'text': '     Зритель\nсам смешно\n     пошутил',
        'font_size': 22,
        'coordinates': [{
            'x': 90,
            'y': 450
        }]
    },  # 1
    {
        'text': '    Зритель\n     уходит\nи это обшу-\n     чивают',
        'font_size': 22,
        'coordinates': [{
            'x': 95,
            'y': 440
        }]
    },  # 2
    {
        'text': 'Участники тей-\n  бла хуесосят\nзрителей за то,\n что они любят\n  юмор тейбла',
        'font_size': 19,
        'coordinates': [{
            'x': 85,
            'y': 435
        }]
    },  # 3
    {
        'text': '    Шутка\n"зритель =\nзаложник"',
        'font_size': 25,
        'coordinates': [{
            'x': 95,
            'y': 445
        }]
    },  # 4
    # Гость
    {
        'text': 'Гость уходит\n     раньше\n  остальных',
        'font_size': 22,
        'coordinates': [{
            'x': 90,
            'y': 455
        }]
    },  # 1
    {
        'text': 'Гость делает\nвид, что учас-\nтники тейбла\n  не ебнутые',
        'font_size': 21,
        'coordinates': [{
            'x': 90,
            'y': 445
        }]
    },  # 2
    {
        'text': '  Гость нахо-\nдится в шоке\n   от уровня\n       юмора',
        'font_size': 21,
        'coordinates': [{
            'x': 90,
            'y': 445
        }]
    },  # 3
    {
        'text': '       Гость\n   пытается\nпонять суть\n         шоу',
        'font_size': 22,
        'coordinates': [{
            'x': 95,
            'y': 440
        }]
    },  # 4
    {
        'text': '       Гость\n   разъебал\nпостоянных\nучастников',
        'font_size': 23,
        'coordinates': [{
            'x': 90,
            'y': 435
        }]
    },  # 5
    {
        'text': 'Гость ищет\nподдержку\n     в зале ',
        'font_size': 23,
        'coordinates': [{
            'x': 95,
            'y': 450
        }]
    },  # 6
    {
        'text': 'Разгон\nгостя в\nпустоту',
        'font_size': 27,
        'coordinates': [{
            'x': 115,
            'y': 440
        }]
    },  # 7
    # Дима
    {
        'text': 'Дима выпил\n    колу до\n  8 минуты\n    записи',
        'font_size': 21,
        'coordinates': [{
            'x': 100,
            'y': 445
        }]
    },  # 1
    {
        'text': '   Дима\nговорит,\nчто Илья\n   идиот',
        'font_size': 24,
        'coordinates': [{
            'x': 110,
            'y': 430
        }]
    },  # 2
    {
        'text': '          Дима\n  допытывает\nпродолжение\n        захода',
        'font_size': 20,
        'coordinates': [{
            'x': 90,
            'y': 440
        }]
    },  # 3
    {
        'text': '       Дима и\n    отсылки к \nОксимирону\nи всем похуй',
        'font_size': 20,
        'coordinates': [{
            'x': 100,
            'y': 445
        }]
    },  # 4
    {
        'text': '       Дима\n     говорит\n"Вы чо суки"',
        'font_size': 24,
        'coordinates': [{
            'x': 90,
            'y': 445
        }]
    },  # 5
    {
        'text': '   Дима\nтребует\n  новый\n  заход',
        'font_size': 28,
        'coordinates': [{
            'x': 105,
            'y': 420
        }]
    },  # 6
    # Илья
    {
        'text': '       Илья -\nвагнеровец',
        'font_size': 24,
        'coordinates': [{
            'x': 90,
            'y': 460
        }]
    },  # 1
    {
        'text': '        Илья\nагрессивно\n    требует\n   смеяться\n    над его\n  шутками',
        'font_size': 20,
        'coordinates': [{
            'x': 105,
            'y': 420
        }]
    },  # 2
    {
        'text': ' Илья\n  бъет\nКостю',
        'font_size': 30,
        'coordinates': [{
            'x': 115,
            'y': 430
        }]
    },  # 3
    {
        'text': '       Илья\nдоводит до\n смешного',
        'font_size': 24,
        'coordinates': [{
            'x': 85,
            'y': 445
        }]
    },  # 4
    {
        'text': '  Илья\nдрочит\nв кадре',
        'font_size': 24,
        'coordinates': [{
            'x': 120,
            'y': 445
        }]
    },  # 5
    {
        'text': ' Илья ебет\n     любых\nродителей ',
        'font_size': 24,
        'coordinates': [{
            'x': 95,
            'y': 445
        }]
    },  # 6
    {
        'text': '             Илья\n     отыгрывает\nмоноспектакль\n           (пенис)',
        'font_size': 19,
        'coordinates': [{
            'x': 85,
            'y': 445
        }]
    },  # 7
    {
        'text': '          Илья\nрассказывает\n    что-то, что\n   становится\n        лором',
        'font_size': 19,
        'coordinates': [{
            'x': 90,
            'y': 435
        }]
    },  # 8
    {
        'text': '       Илья -\n   монолог\nиз фильма',
        'font_size': 24,
        'coordinates': [{
            'x': 95,
            'y': 450
        }]
    },  # 9
    {
        'text': '      Илья\n   сидит в\nтелефоне',
        'font_size': 26,
        'coordinates': [{
            'x': 95,
            'y': 440
        }]
    },  # 10
    # Костя
    {
        'text': ' Костя и\nрубрика\n  "день в\nистории"',
        'font_size': 26,
        'coordinates': [{
            'x': 105,
            'y': 430
        }]
    },  # 1
    {
        'text': '     Костя\nпроверяет\n пишут ли\n   камеры',
        'font_size': 26,
        'coordinates': [{
            'x': 95,
            'y': 430
        }]
    },  # 2
    {
        'text': '          Костя\n   против ебли\nродственников',
        'font_size': 19,
        'coordinates': [{
            'x': 85,
            'y': 455
        }]
    },  # 3
    {
        'text': '     Костя\nскрывает\n    родню',
        'font_size': 26,
        'coordinates': [{
            'x': 95,
            'y': 445
        }]
    },  # 4
    {
        'text': '        Костя\n     говорит\n    зрителям\n"вы больные"',
        'font_size': 22,
        'coordinates': [{
            'x': 90,
            'y': 435
        }]
    },  # 5
    {
        'text': 'Костя и Илья\n    пытаются\n    трахнуть\n  друг друга',
        'font_size': 21,
        'coordinates': [{
            'x': 90,
            'y': 440
        }]
    },  # 6
    {
        'text': '           Костя\n     на озвучке\nпроисходящего',
        'font_size': 18,
        'coordinates': [{
            'x': 85,
            'y': 460
        }]
    },  # 7
    {
        'text': 'Костя обещает\n      причинить\n    физическое\n  насилие Илье',
        'font_size': 18,
        'coordinates': [{
            'x': 93,
            'y': 450
        }]
    },  # 8
    {
        'text': '       Костя\nотыгрывает\n     суицид',
        'font_size': 24,
        'coordinates': [{
            'x': 88,
            'y': 450
        }]
    },  # 9
    {
        'text': '     Костя\nпланирует\n    суицид',
        'font_size': 25,
        'coordinates': [{
            'x': 90,
            'y': 445
        }]
    },  # 10
    {
        'text': 'Костя\n  поет\nхуйню',
        'font_size': 28,
        'coordinates': [{
            'x': 125,
            'y': 435
        }]
    },  # 11
    {
        'text': '  Костя про\nпедофилию',
        'font_size': 22,
        'coordinates': [{
            'x': 90,
            'y': 460
        }]
    },  # 12
    {
        'text': '       Костя\n  смотрит в\n   камеру с\nбезнадегой',
        'font_size': 22,
        'coordinates': [{
            'x': 90,
            'y': 435
        }]
    },  # 13
]


async def generate_image(phrases: dict, img: str, a=0, b=0, c=0, x=0, y=0):
    # generate random number
    num = randint(1, 3)

    # open random image
    image = Image.open(f"background/{num}.png")

    # creating a filter list
    indices = []

    # cell filling
    while a < 25:
        # generate index
        i = randint(0, len(phrases) - 1)

        # adding text to cells
        if i not in indices:
            a += 1

            # loop
            if a == 1:
                x = phrases[i]['coordinates'][0]['x']
                y = phrases[i]['coordinates'][0]['y']
            elif a in [2, 3, 4, 5]:
                b += 196
                x = phrases[i]['coordinates'][0]['x'] + b
                y = phrases[i]['coordinates'][0]['y']
            elif a == 6:
                c += 165
                b = 0
                x = phrases[i]['coordinates'][0]['x']
                y = phrases[i]['coordinates'][0]['y'] + c
            elif a in [7, 8, 9, 10]:
                b += 196
                x = phrases[i]['coordinates'][0]['x'] + b
                y = phrases[i]['coordinates'][0]['y'] + c
            elif a == 11:
                c += 185
                b = 0
                x = phrases[i]['coordinates'][0]['x']
                y = phrases[i]['coordinates'][0]['y'] + c
            elif a in [12, 13, 14, 15]:
                b += 196
                x = phrases[i]['coordinates'][0]['x'] + b
                y = phrases[i]['coordinates'][0]['y'] + c
            elif a == 16:
                c += 175
                b = 0
                x = phrases[i]['coordinates'][0]['x']
                y = phrases[i]['coordinates'][0]['y'] + c
            elif a in [17, 18, 19, 20]:
                b += 196
                x = phrases[i]['coordinates'][0]['x'] + b
                y = phrases[i]['coordinates'][0]['y'] + c
            elif a == 21:
                c += 175
                b = 0
                x = phrases[i]['coordinates'][0]['x']
                y = phrases[i]['coordinates'][0]['y'] + c
            elif a in [22, 23, 24, 25]:
                b += 196
                x = phrases[i]['coordinates'][0]['x'] + b
                y = phrases[i]['coordinates'][0]['y'] + c

            # select font
            font = ImageFont.truetype('font/Unbounded-Regular.ttf', phrases[i]['font_size'])

            # font color selection
            if num == 3:
                fill = 'black'
            else:
                fill = 'white'

            # adding text to the background
            drawer = ImageDraw.Draw(image)
            drawer.text((x, y), phrases[i]['text'], font=font, fill=fill)

            # adding an index to a list
            indices.append(i)

        # clear list
        if a == 25:
            indices.clear()

    # save image
    image.save(f'img/{img}.png')