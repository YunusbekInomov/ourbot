import requests
from telegram import ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from nbucurrency import nbuCurrency
from sqbcurrency import sqbCurrency

# url="https://nbu.uz/exchange-rates/json/"
# response = requests.get(url)
# data = response.json()
buttons = ReplyKeyboardMarkup([['Valyuta kurslari']], resize_keyboard=True)
nbucurrency = nbuCurrency()
sqbcurrency = sqbCurrency()
def start(update, context) -> None:
    update.message.reply_html(f'Assalomu alekum <b>{update.effective_user.first_name}!</b>', reply_markup=buttons)
    return 1
data_nbu = nbucurre ncy.getCurrency()
data_sqb = sqbcurrency.getCurrency()
# print(data_sqb)
def bank(update, context):
    buttons = ReplyKeyboardMarkup([['NBU','SQB'],['Asosiy']], resize_keyboard=True)
    update.message.reply_text(f'Bank turini tanlang!', reply_markup=buttons)

def currence_nbu(update, context):
    buttons = ReplyKeyboardMarkup([['USD vs UZS','RUB vs UZS','KZT vs UZS'],['CHF vs UZS','JPY vs UZS','EUR vs UZS'],['Asosiy']], resize_keyboard=True)
    update.message.reply_text(f'Valyuta turini tanlang!', reply_markup=buttons)
    global bank
    bank = 'nbu'

def currence_sqb(update, context):
    buttons = ReplyKeyboardMarkup([['USD vs UZS','EUR vs UZS','RUB vs UZS'],['GBP vs UZS','JPY vs UZS','CHF vs UZS'],['Asosiy']], resize_keyboard=True)
    update.message.reply_text(f'Valyuta turini tanlang!', reply_markup=buttons)
    global bank
    bank = 'sqb'

def currenusd(update, context):
    buttons = ReplyKeyboardMarkup([['USD ⬇️','USD ⬆️','↩️']], resize_keyboard=True)
    update.message.reply_text(f'Alishtirish turini tanlang!', reply_markup=buttons)
    global code
    code = 'USD'

def currenrub(update, context):
    buttons = ReplyKeyboardMarkup([['RUB ⬇️','RUB ⬆️','↩️']], resize_keyboard=True)
    update.message.reply_text(f'Alishtirish turini tanlang!', reply_markup=buttons)
    global code
    code = 'RUB'

def currenkzt(update, context):
    buttons = ReplyKeyboardMarkup([['KZT ⬇️','KZT ⬆️','↩️']], resize_keyboard=True)
    update.message.reply_text(f'Alishtirish turini tanlang!', reply_markup=buttons)
    global code
    code = 'KZT'

def currenchf(update, context):
    buttons = ReplyKeyboardMarkup([['CHF ⬇️','CHF ⬆️','↩️']], resize_keyboard=True)
    update.message.reply_text(f'Alishtirish turini tanlang!', reply_markup=buttons)
    global code
    code = 'CHF'

def currenjpy(update, context):
    buttons = ReplyKeyboardMarkup([['JPY ⬇️','JPY ⬆️','↩️']], resize_keyboard=True)
    update.message.reply_text(f'Alishtirish turini tanlang!', reply_markup=buttons)
    global code
    code = 'JPY'

def curreneur(update, context):
    buttons = ReplyKeyboardMarkup([['EUR ⬇️','EUR ⬆️','↩️']], resize_keyboard=True)
    update.message.reply_text(f'Alishtirish turini tanlang!', reply_markup=buttons)
    global code
    code = 'EUR'

def currencell(update, context):
    buttons = ReplyKeyboardMarkup([['{} ⬇️'.format(code),'{} ⬆️'.format(code),'↩️']], resize_keyboard=True)
    buy = '⬇️'
    img = '⏱'
    conv_img = '🔄'
    if bank == 'sqb':
        data = data_sqb
        back = currence_sqb
    elif bank == 'nbu':
        data = data_nbu
        back = currence_nbu

    for x in data:
        if bank == 'sqb':
            cell_data = x['cell_price']
        elif bank == 'nbu':
            cell_data = x['nbu_cell_price']

        if x['code'] == code:
            update.message.reply_html('<b>{}</b> {}: <b>{}\n\n{} </b>{} <b>1:</b><b>  {}  </b><b>{}:</b> UZS'.format(x['title'],img,x['date'],buy,x['code'],conv_img,cell_data), reply_markup=buttons)
        # code = x['code']
def currenbuy(update, context):
    buttons = ReplyKeyboardMarkup([['{} ⬇️'.format(code),'{} ⬆️'.format(code),'↩️']], resize_keyboard=True)
    cell = '⬆️'
    img = '⏱'
    conv_img = '🔄'
    if bank == 'sqb':
        data = data_sqb
        back = currence_sqb
    elif bank == 'nbu':
        data = data_nbu
        back = currence_nbu

    for x in data:
        if bank == 'sqb':
            buy_data = x['buy_price']
        elif bank == 'nbu':
            buy_data = x['nbu_buy_price']

        if x['code'] == code:
            update.message.reply_html('<b>{}</b> {}: <b>{}\n\n{} </b>{} <b>1:</b><b>  {}  </b><b>{}:</b> UZS'.format(x['title'],img,x['date'],cell,x['code'],conv_img,buy_data), reply_markup=buttons)
        # code = x['code']

updater = Updater('1937889820:AAEAL1o9jmWyWiH_Ejmn8IPXzxrMgYt7yn0', use_context = True)

conv_handler = ConversationHandler(
    entry_points = [CommandHandler('start', start),CommandHandler('Asosiy', start)],
    states = {
        1:{
            MessageHandler(Filters.regex('^(Valyuta kurslari)$'), bank),
            MessageHandler(Filters.regex('^(NBU)$'), currence_nbu),
            MessageHandler(Filters.regex('^(SQB)$'), currence_sqb),
            MessageHandler(Filters.regex('^(USD vs UZS)$'), currenusd),
            MessageHandler(Filters.regex('^(RUB vs UZS)$'), currenrub),
            MessageHandler(Filters.regex('^(KZT vs UZS)$'), currenkzt),
            MessageHandler(Filters.regex('^(CHF vs UZS)$'), currenchf),
            MessageHandler(Filters.regex('^(JPY vs UZS)$'), currenjpy),
            MessageHandler(Filters.regex('^(EUR vs UZS)$'), curreneur),
            MessageHandler(Filters.regex('^(USD ⬇️)$'), currencell),
            MessageHandler(Filters.regex('^(USD ⬆️)$'), currenbuy),
            MessageHandler(Filters.regex('^(RUB ⬇️)$'), currencell),
            MessageHandler(Filters.regex('^(RUB ⬆️)$'), currenbuy),
            MessageHandler(Filters.regex('^(KZT ⬇️)$'), currencell),
            MessageHandler(Filters.regex('^(KZT ⬆️)$'), currenbuy),
            MessageHandler(Filters.regex('^(CHF ⬇️)$'), currencell),
            MessageHandler(Filters.regex('^(CHF ⬆️)$'), currenbuy),
            MessageHandler(Filters.regex('^(JPY ⬇️)$'), currencell),
            MessageHandler(Filters.regex('^(JPY ⬆️)$'), currenbuy),
            MessageHandler(Filters.regex('^(EUR ⬇️)$'), currencell),
            MessageHandler(Filters.regex('^(EUR ⬆️)$'), currenbuy),
            MessageHandler(Filters.regex('^(↩️)$'), bank)
        }
    },
    fallbacks = [MessageHandler(Filters.text, start)]
)

updater.dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()

#valyuta 60da94087b439980e6c49674