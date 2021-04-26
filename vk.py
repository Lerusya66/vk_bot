import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import requests


def write_msg(user_id, message, random_id):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': get_random_id()})


n = 0
# API-ключ созданный ранее
token = "35d3f15e77bf2d53a360afc11c3338fc803a238f73a606bfa559582fe2d93bb602b578b2c0d08bd7820e1"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Хай", get_random_id())

            elif 'грустно' in request or 'sad' in request:
                write_msg(event.user_id, "Всё обязательно будет хорошо! Номер центра поддержки: +7 (499) 173-09-09",
                          get_random_id())

            elif request == "пока":
                write_msg(event.user_id, "Пока((", get_random_id())

            elif 'квест' in request:
                write_msg(event.user_id, "Я очень рад, что ты спросил", get_random_id())

            elif 'стать' in request and 'друг' in request:
                d = open('another article.txt', 'r', encoding='utf-8').read()
                write_msg(event.user_id, "Да, это определенно не всё, что у меня есть", get_random_id())

                write_msg(event.user_id, d, get_random_id())

            elif 'стать' in request:
                d = open('data_article.txt', 'r', encoding='utf-8').read()
                write_msg(event.user_id, "Я очень рад, что ты спросил", get_random_id())

                write_msg(event.user_id, d, get_random_id())

            elif request == "обзывательства":
                vk.method('messages.send', {'user_id': event.user_id, 'message': ' fly',
                                            'attachment': "photo-204239926_457239019", 'random_id': get_random_id()})

            elif request == "у меня всё получится?":

                vk.method('messages.send',
                          {'user_id': event.user_id, 'message': ' конечно, солнце',
                           'attachment': "photo-204239926_457239021",
                           'random_id': get_random_id()})



            elif 'решишь пример?' in request:
                vk.method('messages.send',
                          {'user_id': event.user_id, 'message': ' конечно, солнце',
                           'random_id': get_random_id()})

            elif request == 'ты тоже молодец!':
                vk.method('messages.send',
                          {'user_id': event.user_id, 'message': 'Ты мой самый лучший человек!',
                           'random_id': get_random_id()})

            elif request == 'хорошую музыку':
                vk.method('messages.send',
                          {'user_id': event.user_id, 'message': 'Для тебя всегда да',
                           'attachment': "wall-204239926_4",
                           'random_id': get_random_id()})


            elif request == 'давай другую':
                vk.method('messages.send',
                          {'user_id': event.user_id, 'message': 'конечно, зай',
                           'attachment': "wall-204239926_5",
                           'random_id': get_random_id()})

            elif request == 'хочу резы моша':
                vk.method('messages.send',
                          {'user_id': event.user_id, 'message': 'конечно, зай',
                           'attachment': "wall-204239926_6",
                           'random_id': get_random_id()})



            elif request == 'какая песня твоя самая любимая?':
                d = open('my dear.txt').read()
                vk.method('messages.send',
                          {'user_id': event.user_id, 'message': f'я рад, что ты спросил\n{d}',
                           'attachment': "wall-204239926_8",
                           'random_id': get_random_id()})

            elif 'н/нн' in request:
                vk.method('messages.send',
                          {'user_id': event.user_id, 'message': f'я рад, что ты спросил',
                           'attachment': "wall-204239926_9",
                           'random_id': get_random_id()})
            elif 'шутк' in request:
                d = open('шутки.txt', 'r').read()
                vk.method('messages.send',
                          {'user_id': event.user_id, 'message': f'я рад, что ты спросил\n{d}',
                           'attachment': "wall-204239926_9",
                           'random_id': get_random_id()})
            elif 'клоун' in request:
                vk.method('messages.send',
                          {'user_id': event.user_id, 'message': f'ответ прост -- Арман',
                           'attachment': "wall-204239926_9",
                           'random_id': get_random_id()})
            elif 'биолог' in request:
                vk.method('messages.send',
                          {'user_id': event.user_id, 'message': f'Если бы вы прочитали в газете сообщение о том, '
                                                                f'что профессор Андреев создал лекарство от обычной простуды '
                                                                f'и был награжден государственной премией, то были бы вы '
                                                                f'уверены в том, что это достоверный научный факт? '
                                                                f'Приведите аргументы в пользу своего ответа.',
                           'attachment': "wall-204239926_9",
                           'random_id': get_random_id()})
            elif 'проверить' in request:
                vk.method('messages.send',
                          {'user_id': event.user_id,
                           'message': f'well done',
                           'attachment': "photo-204239926_457239021",
                           'random_id': get_random_id()})
            elif 'крутой плейлист слабо?' in request:
                vk.method('messages.send',
                          {'user_id': event.user_id,
                           'message': f'https://music.yandex.ru/album/2840969/track/24387554?from=serp_lyrics_bound',
                           'attachment': "photo-204239926_457239021",
                           'random_id': get_random_id()})
            elif 'где ты берешь эти тупые анекдоты?' in request:
                vk.method('messages.send',
                          {'user_id': event.user_id, 'message': f'https://anekdotbar.ru/',
                           'attachment': "photo-204239926_457239021",
                           'random_id': get_random_id()})

            elif 'прочитай мне стихи' in request:
                vk.method('messages.send',
                          {'user_id': event.user_id, 'message': f"""Среди других играющих детей
Она напоминает лягушонка.
Заправлена в трусы худая рубашонка,
Колечки рыжеватые кудрей
Рассыпаны, рот длинен, зубки кривы,
Черты лица остры и некрасивы.
Двум мальчуганам, сверстникам её,
Отцы купили по велосипеду.
Сегодня мальчики, не торопясь к обеду,
Гоняют по двору, забывши про неё,
Она ж за ними бегает по следу.
Чужая радость так же, как своя,
Томит её и вон из сердца рвётся,
И девочка ликует и смеётся,
Охваченная счастьем бытия.

Ни тени зависти, ни умысла худого
Ещё не знает это существо.
Ей всё на свете так безмерно ново,
Так живо всё, что для иных мертво!
И не хочу я думать, наблюдая,
Что будет день, когда она, рыдая,
Увидит с ужасом, что посреди подруг
Она всего лишь бедная дурнушка!
Мне верить хочется, что сердце не игрушка,
Сломать его едва ли можно вдруг!
Мне верить хочется, что чистый этот пламень,
Который в глубине её горит,
Всю боль свою один переболит
И перетопит самый тяжкий камень!
И пусть черты её нехороши
И нечем ей прельстить воображенье,-
Младенческая грация души
Уже сквозит в любом её движенье.
А если это так, то что есть красота
И почему её обожествляют люди?
Сосуд она, в котором пустота,
Или огонь, мерцающий в сосуде?
""",
                           'attachment': "photo-204239926_457239021",
                           'random_id': get_random_id()})



            elif request.isalpha() is False:
                vk.method('messages.send',
                          {'user_id': event.user_id, 'message': eval(request),
                           'random_id': get_random_id()})


            else:
                write_msg(event.user_id, "Не поняла вашего ответа...", get_random_id())
            # счетчик слова "вот"
            if 'вот' in request:
                n += 1
                write_msg(event.user_id, f"следи за базаром! уже {n} раз сказала вот", get_random_id())
