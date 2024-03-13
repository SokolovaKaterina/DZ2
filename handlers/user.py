import telebot
from telebot.handler_backends import StatesGroup, State

from funcs.datatime import gel_welcome
from funcs.functionality import functionality
from funcs.functionality2 import functionality2
from init_bot import bot


class UserState(StatesGroup):
    state1 = State()


@bot.message_handler(commands=["start", "help"])
def start(message: telebot.types.Message):
    text = f"{gel_welcome()} \n" \
           f"Я бот-помощник для университета🏛\n\n" \
           f"Вот что я имею:\n" \
           f"{functionality()}"
    bot.send_message(message.chat.id, text)
    bot.set_state(message.from_user.id, UserState.state1)


@bot.message_handler(commands=["get_info"], state=UserState.state1)
def get_info(message: telebot.types.Message):
    text = f"Чем я могу помочь?👩🏻‍🎓\n" \
           f"{functionality2()}"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["get_directorate"])
def get_directorate(message: telebot.types.Message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2)
    markup.add(
        telebot.types.KeyboardButton("ИТС"),
        telebot.types.KeyboardButton("ИФХТиМ"),
        telebot.types.KeyboardButton("ИНЭЛ"),
        telebot.types.KeyboardButton("ИЯЭиТФ"),
        telebot.types.KeyboardButton("ИРИТ"),
        telebot.types.KeyboardButton("ИПТМ"),
        telebot.types.KeyboardButton("ИНЭУ")

    )
    bot.reply_to(message, "Информацию о дирекции какого института Вам нужно предоставить?", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "ИТС")
def handle_action(message: telebot.types.Message):
    markup = telebot.util.quick_markup({
        "Группа в ВК": {"url": "https://vk.com/its_ngtu"},
        "Сайт": {"url": "https://www.nntu.ru/structure/view/podrazdeleniya/its"}
    })
    bot.reply_to(message, "Вот необходимые ссылки о дирекции ИТС:", reply_markup=markup)
    bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
    bot.clear_reply_handlers_by_message_id(message.message_id)


@bot.message_handler(func=lambda message: message.text == "ИФХТиМ")
def handle_action(message: telebot.types.Message):
    markup = telebot.util.quick_markup({
        "Группа в ВК": {"url": "https://vk.com/ifhtim"},
        "Сайт": {"url": "https://www.nntu.ru/structure/view/podrazdeleniya/ifhtim"}
    })
    bot.reply_to(message, "Вот необходимые ссылки о дирекции ИФХТиМ:", reply_markup=markup)
    bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
    bot.clear_reply_handlers_by_message_id(message.message_id)


@bot.message_handler(func=lambda message: message.text == "ИНЭЛ")
def handle_action(message: telebot.types.Message):
    markup = telebot.util.quick_markup({
        "Группа в ВК": {"url": "https://vk.com/inel_ngtu"},
        "Сайт": {"url": "https://www.nntu.ru/structure/view/podrazdeleniya/inel"}
    })
    bot.reply_to(message, "Вот необходимые ссылки о дирекции ИНЭЛ:", reply_markup=markup)
    bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
    bot.clear_reply_handlers_by_message_id(message.message_id)


@bot.message_handler(func=lambda message: message.text == "ИЯЭиТФ")
def handle_action(message: telebot.types.Message):
    markup = telebot.util.quick_markup({
        "Группа в ВК": {"url": "https://vk.com/nnstu_ftf"},
        "Сайт": {"url": "https://www.nntu.ru/structure/view/podrazdeleniya/iyaeitf"}
    })
    bot.reply_to(message, "Вот необходимые ссылки о дирекции ИЯЭиТФ:", reply_markup=markup)
    bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
    bot.clear_reply_handlers_by_message_id(message.message_id)


@bot.message_handler(func=lambda message: message.text == "ИРИТ")
def handle_action(message: telebot.types.Message):
    markup = telebot.util.quick_markup({
        "Группа в ВК": {"url": "https://vk.com/irit_official"},
        "Сайт": {"url": "https://www.nntu.ru/structure/view/podrazdeleniya/irit"}
    })
    bot.reply_to(message, "Вот необходимые ссылки о дирекции ИРИТ:", reply_markup=markup)
    bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
    bot.clear_reply_handlers_by_message_id(message.message_id)


@bot.message_handler(func=lambda message: message.text == "ИПТМ")
def handle_action(message: telebot.types.Message):
    markup = telebot.util.quick_markup({
        "Группа в ВК": {"url": "https://vk.com/ngtuiptm"},
        "Сайт": {"url": "https://www.nntu.ru/structure/view/podrazdeleniya/iptm"}
    })
    bot.reply_to(message, "Вот необходимые ссылки о дирекции ИПТМ:", reply_markup=markup)
    bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
    bot.clear_reply_handlers_by_message_id(message.message_id)


@bot.message_handler(func=lambda message: message.text == "ИНЭУ")
def handle_action(message: telebot.types.Message):
    markup = telebot.util.quick_markup({
        "Группа в ВК": {"url": "https://vk.com/ineungtu"},
        "Сайт": {"url": "https://www.nntu.ru/structure/view/podrazdeleniya/ineu"}
    })
    bot.reply_to(message, "Вот необходимые ссылки о дирекции ИНЭУ:", reply_markup=markup)
    bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
    bot.clear_reply_handlers_by_message_id(message.message_id)


@bot.message_handler(commands=["get_url"])
def get_url(message: telebot.types.Message):
    markup = telebot.util.quick_markup({
        "Личный кабинет": {
            "url": "https://auth.nntu.ru/idp/oauth2_login.jsp#/provider/LDAP/12ef96388641343f28b7d5bd10cf430e"}
    })
    bot.reply_to(message, "Вот ссылка на личный кабинет учащегося/сотрудника НГТУ им. Р.Е.Алексеева:",
                 reply_markup=markup)
    bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
    bot.clear_reply_handlers_by_message_id(message.message_id)


@bot.message_handler(commands=["get_lk"])
def get_lk(message: telebot.types.Message):
    markup = telebot.util.quick_markup({
        "Сайт университета": {"url": "https://www.nntu.ru/"}
    })
    bot.reply_to(message, "Вот ссылка на сайт НГТУ им. Р.Е.Алексеева:", reply_markup=markup)
    bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
    bot.clear_reply_handlers_by_message_id(message.message_id)


@bot.message_handler(commands=["end"], state=UserState.state1)
def end(message: telebot.types.Message):
    markup = telebot.types.ReplyKeyboardRemove()
    text = f"Спасибо! Пока)"
    bot.send_message(message.chat.id, text, reply_markup=markup)
    bot.delete_state(message.from_user.id)
