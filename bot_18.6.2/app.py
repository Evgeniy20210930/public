import telebot
from config import keys, TOKEN
from extensions import ConvertionException, СurrencyConverter
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text = 'Для начала работы введите команду в формате: \n<наименование валюты> \
\n<в какую валюту конвертировать> \
\n<количество переводимой валюты>\nПосмотреть список доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text,key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) !=3:
           raise ConvertionException('Лишние параметры')
        base, quote, amount = values
        total_base = СurrencyConverter.get_price(base, quote, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {base} в {quote} - {round(float(total_base)*float(amount),2)}'
        bot.send_message(message.chat.id, text)

bot.polling()
