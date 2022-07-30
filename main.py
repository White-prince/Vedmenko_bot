import vk_api
from config import TOKEN, admin_id, admin_id_2, admin_id_3
from words import word
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

session = vk_api.VkApi(token=TOKEN)
session_api = session.get_api()
longpoll = VkLongPoll(session)


def send_some_msg(id_user, message, keyboard=None):
    post = {'user_id': id_user, 'message': message, 'random_id': 0}
    if keyboard is not None:
        post['keyboard'] = keyboard.get_keyboard()
    else:
        pass
    session.method("messages.send", post)


def ads():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Заказать рекламный ролик', VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('На главную', VkKeyboardColor.SECONDARY)
    send_some_msg(user_id, "Эксклюзивный видеоролик сделает ваш бренд узнаваемым,"
                           " привлечет большее количество потенциальных клиентов. "
                           "Наша команда создаст качественный видео-контент,"
                           " который будет отличаться на фоне конкурентов.\n"
                           "Стоимость: от 18 500₽", keyboard)


def clip():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Заказать съемку видеоклипа', VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('На главную', VkKeyboardColor.SECONDARY)
    send_some_msg(user_id, "Уникальный и стильный клип, который будет неповторимым и повысит узнаваемость артиста. "
                           "Наша команда создаст творческий клип по всем трендам индустрии,"
                           " что не оставит равнодушным зрителя.\n"
                           "Стоимость: от 10 500₽", keyboard)


def film():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('заказать короткометражный фильм', VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('На главную', VkKeyboardColor.SECONDARY)
    send_some_msg(user_id, "Создания короткометражного фильма по вашему сценарию или под ключ. "
                           "Наша команда обладает свежим и прогрессивным мышлением, "
                           "что позволяет создать умное и важное кино.\n"
                           "Стоимость: от 100 000₽", keyboard)


def buy_ads(message):
    if message == "заказать рекламный ролик":
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_openlink_button(label='Перейти на сайт', link='https://vedmenkoprod.ru/')
        keyboard.add_line()
        keyboard.add_button('На главную', VkKeyboardColor.SECONDARY)
        send_some_msg(user_id,
                      "Сделать заказ вы можете, через наш сайт или задать вопрос и наша команда ответит"
                      " вам и обработает ваш заказ", keyboard)


def buy_clip(message):
    if message == "заказать съемку видеоклипа":
        keyboard = VkKeyboard(one_time=False)
        keyboard.add_openlink_button(label='Перейти на сайт', link='https://vedmenkoprod.ru/')
        keyboard.add_line()
        keyboard.add_button('На главную', VkKeyboardColor.SECONDARY)
        send_some_msg(user_id,
                      "Сделать заказ вы можете, через наш сайт или задать вопрос и наша команда ответит"
                      " вам и обработает ваш заказ", keyboard)


def buy_film(message):
    if message == "заказать короткометражный фильм":
        keyboard = VkKeyboard(one_time=False)
        keyboard.add_openlink_button(label='Перейти на сайт', link='https://vedmenkoprod.ru/')
        keyboard.add_line()
        keyboard.add_button('На главную', VkKeyboardColor.SECONDARY)
        send_some_msg(user_id,
                      "Сделать заказ вы можете, через наш сайт или задать вопрос и наша команда ответит"
                      " вам и обработает ваш заказ", keyboard)


def get_back():
    if msg == "на главную":
        keyboard = VkKeyboard(one_time=False)
        keyboard.add_button('Задать вопрос', VkKeyboardColor.SECONDARY)
        keyboard.add_button('Сделать заказ', VkKeyboardColor.SECONDARY)
        keyboard.add_line()
        keyboard.add_openlink_button(label='Перейти на сайт', link='https://vedmenkoprod.ru/')
        send_some_msg(user_id, "Что вас интересует?", keyboard)


def send_question():
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_openlink_button(label='Перейти в чаты', link='https://vk.com/gim160010948?peers=303218316')
    send_some_msg(admin_id, "Пришел вопрос", keyboard)
    send_some_msg(admin_id_2, "Пришел вопрос", keyboard)
    send_some_msg(admin_id_3, "Пришел вопрос", keyboard)


def greater(message):
    for i in word:
        if message == i:
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Начать', VkKeyboardColor.PRIMARY)
            send_some_msg(user_id, "Здравствуйте, Vedmenko Production - это молодой, перспективный Видеопродакшн."
                                   " Наша команда делает творческий и качественный фото-видеоконтент,"
                                   " который популяризирует ваш бренд, привлекает большое количество клиентов"
                                   " и дарит много позитивных эмоций от готового продукта."
                                   " Для начала работы нажмите на кнопку 'Начать'.", keyboard)


if __name__ == '__main__':
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msg = event.text.lower()
            user_id = event.user_id
            greater(msg)
            get_back()
            buy_ads(msg)
            buy_clip(msg)
            buy_film(msg)
            if msg == "начать":
                keyboard = VkKeyboard(one_time=False)
                keyboard.add_button('Задать вопрос', VkKeyboardColor.SECONDARY)
                keyboard.add_button('Сделать заказ', VkKeyboardColor.SECONDARY)
                keyboard.add_line()
                keyboard.add_openlink_button(label='Перейти на сайт', link='https://vedmenkoprod.ru/')
                send_some_msg(user_id, "Чем мы можем вам помочь?"
                                       " Для получения большей информации о нас или заказе услуг"
                                       " перейдите на наш сайт", keyboard)
            if msg == "задать вопрос":
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button('На главную', VkKeyboardColor.SECONDARY)
                send_some_msg(user_id, "Задайте свой вопрос")
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                        send_some_msg(user_id, "Спасибо за ваш вопрос. "
                                               "Мы ответим на него в течении 24 часов", keyboard)
                        send_question()
                        break
            if msg == "сделать заказ":
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button('Рекламный ролик', VkKeyboardColor.POSITIVE)
                keyboard.add_button('Снять видеоклип', VkKeyboardColor.POSITIVE)
                keyboard.add_line()
                keyboard.add_button('Короткометражный фильм', VkKeyboardColor.POSITIVE)
                keyboard.add_line()
                keyboard.add_button('На главную', VkKeyboardColor.SECONDARY)
                send_some_msg(user_id, "Выберите интересующую вас услугу", keyboard)
            if msg == "рекламный ролик":
                ads()
            if msg == "снять видеоклип":
                clip()
            if msg == "короткометражный фильм":
                film()
