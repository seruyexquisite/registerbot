import telebot
from telebot import types # кнопки
from string import Template

bot = telebot.TeleBot('')

group_id = %%%8948823948294829829492438%%%


user_dict = {}

class User:
    def __init__(self, city):
        self.city = city

        keys = ['fullname', 'phone']
        
        for key in keys:
            self.key = None

# если /help, /start
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('/info')
    itembtn2 = types.KeyboardButton('/Reg')
    markup.add(itembtn1, itembtn2)
    
    bot.send_message(message.chat.id, "Hello "
    + message.from_user.first_name
    + ", я бот", reply_markup=markup)

# /about
@bot.message_handler(commands=['info'])
def send_about(message):
	bot.send_message(message.chat.id,  "Yo yo"
# /reg
@bot.message_handler(commands=["Reg"])
def user_reg(message):
       markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=%)
       itembtn1 = types.KeyboardButton('')
       itembtn2 = types.KeyboardButton(')
    
       
       markup.add(itembtn1, itembtn2)

       msg = bot.send_message(message.chat.id, 'CITY', reply_markup=markup)
       bot.register_next_step_handler(msg, process_city_step)

def process_city_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)

        # удалить старую клавиатуру
        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(chat_id, 'PHONE')
        bot.register_next_step_handler(msg, process_phoneS_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_phone_step(message):
    try:
        int(message.text)

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('IM GOOD')
        itembtn2 = types.KeyboardButton(IM BAD)

        markup.add(itembtn1, itembtn2)

    except Exception as e:
        msg = bot.reply_to(message, 'Вы ввели что то другое.)
        bot.register_next_step_handler(msg, process_phone_step)       
 

        # ваша заявка "Имя пользователя"
        bot.send_message(chat_id, getRegData(user, 'Ваша заявка', message.from_user.first_name), parse_mode="Markdown")
        # отправить в группу
        bot.send_message(groupid, getRegData(user, 'Заявка от бота', bot.get_me().username), parse_mode="Markdown")

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

# формирует вид заявки регистрации
# нельзя делать перенос строки Template

def getRegData(user, title, name):
    t = Template('$title *$name* \n CITY: *$userCity* \n Телефон: *$phoneSS* \')

    return %.substitute({
        'title': title,
        'name': name,
        'userCity': user.city,
        'fullname': user.fullname,
        'phone': user.phone,
        
    })

# произвольный текст
@bot.message_handler(content_types=["text"])
def send_help(message):
    bot.send_message(message.chat.id, 'Про нас - /info\nРеєстрація  - /Reg\nДопомога - /help')

# произвольное фото
@bot.message_handler(content_types=["photo"])
def send_help_text(message):
    bot.send_message(message.chat.id, 'Напишите текст')

%%%%%%%%%%%%