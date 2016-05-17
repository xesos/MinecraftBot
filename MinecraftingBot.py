import sys
import time
import telepot
import telepot.namedtuple
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardHide, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent

def handle(msg):

    content_type, chat_type, chat_id = telepot.glance(msg)
    m = telepot.namedtuple.Message(**msg)

    if chat_id < 0:
        # group message
        print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
    else:
        # private message
        print 'Received a %s from %s' % (content_type, m.chat)  # m.chat == m.from_
    message = msg['text'].encode('unicode-escape').decode('ascii')
    if message == '/start':
        # For long messages, only return the first 10 characters.
        # Length-checking and substring-extraction may work differently
        # depending on Python versions and platforms. See above.
        markup = ReplyKeyboardMarkup(keyboard=[
                     ['Blocks', 'Decoration','Redstone'],
                     ['Transportation', 'Miscellanous','Foodstuff'],
                     ['Tools', 'Combat','Brewing','Materials'],
                 ])
        bot.sendMessage(chat_id, 'Select the category of element you want to craft', reply_markup=markup)
    if message == 'Blocks':
        markup2 = ReplyKeyboardMarkup(keyboard=[
                     ['Stone'],
                 ])
        bot.sendMessage(chat_id, 'Select element to craft', reply_markup=markup2)
    if message == 'Stone':
        f = open("images/craft_stonebrick.png",'rb')
        bot.sendPhoto(chat_id, f)
                


TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)


print 'Listening ...'

# Keep the program running.
while 1:
    time.sleep(10)
