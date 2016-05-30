import sys
import time
import os.path
from difflib import SequenceMatcher
import telepot
import telepot.namedtuple
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardHide, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent


def handle(msg):

    content_type, chat_type, chat_id = telepot.glance(msg)
    m = telepot.namedtuple.Message(**msg)
    with open('objects.txt') as f:
    	objects = f.read().splitlines()

    if chat_id < 0:
        # group message
        print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
    else:
        # private message
        print 'Received a %s from %s' % (content_type, m.chat)  # m.chat == m.from_
    message = msg['text'].encode('unicode-escape').decode('ascii')
    if message == '/start' or message == 'Back':
        # For long messages, only return the first 10 characters.
        # Length-checking and substring-extraction may work differently
        # depending on Python versions and platforms. See above.
        markup = ReplyKeyboardMarkup(keyboard=[
                     ['Blocks', 'Decoration','Redstone'],
                     ['Transportation', 'Miscellanous','Foodstuff'],
                     ['Tools', 'Combat','Brewing','Materials'],
                 ])
        bot.sendMessage(chat_id, 'Select the category of element you want to craft', reply_markup=markup)
    elif message == 'Blocks':
        markup2 = ReplyKeyboardMarkup(keyboard=[
                     ['Stone brick', 'Wood', 'Polished granite'],
                     ['Polished andesite', 'Polished diorite', ],
                     ['Stone slabs', 'Sanstone', 'Block of coal'],
                     ['Block of Quartz', 'Block of redstone', 'Iron block'],
                     ['Pillar quartz block', 'Nether brick', 'Mossys stone brick'],
                     ['Moss stone', 'Melon block', 'Dark prismarine'],
                     ['Chiseled red sandstone', 'Chiseled quartz block', 'Chiseled stone brick'],
                     ['Decorative sandstone','Emerald block','Diamond block','Back'],
                 ])
        bot.sendMessage(chat_id, 'Select element to craft', reply_markup=markup2)
    elif message == 'Decoration':
        markup2 = ReplyKeyboardMarkup(keyboard=[
                     ['Bed', 'Torch', 'Chest','Furnace'],
                     ['Sign', 'Ladder', 'Snow', 'Anvil'],
                     ['Jukebox', 'Fence', 'Stone stairs', 'Glass panes'],
                     ['Carpets', 'Banner', 'Fence gate', 'Painting'],
                     ['Item frame', 'Doors', 'Armor stand', 'Wooden stairs'],
                     ['Enchantement table', 'Ender chest','Flower pot','Back'],
                 ])
        bot.sendMessage(chat_id, 'Select element to craft', reply_markup=markup2)
    elif message == 'Redstone':
        markup2 = ReplyKeyboardMarkup(keyboard=[
                     ['Note block','Powered rail','Detector rail', 'Boat'],
                     ['Sticky piston', 'TNT', 'Doors', 'Fence'],
                     ['Redstone lamp', 'Tripwire hook', 'Button'],
                     ['Redstone comparator', 'Daylight sensor', 'Hopper'],
                     ['Dropper', 'Repeater', 'Redstone comparator'],
                     ['Redstone torch', 'Trapdoor','Pressure plates','Back'],
                 ])
        bot.sendMessage(chat_id, 'Select element to craft', reply_markup=markup2)
    elif message == 'Transportation':
        markup2 = ReplyKeyboardMarkup(keyboard=[
                     ['Tracks','Activator rail','Minecart', 'Boat'],
                     ['Minecart with hopper', 'Minecart with tnt'],
                     ['Carrot on a stick', 'Firework','Back'],
                 ])
        bot.sendMessage(chat_id, 'Select element to craft', reply_markup=markup2)
    elif message == 'Miscellanous':
        markup2 = ReplyKeyboardMarkup(keyboard=[
                     ['Beacon','Bucket','Snow', 'Fire Charge'],
                     ['Paper', 'Book','Slime Block', 'Book and Quill'],
                     ['Map', 'Eye of Ender', 'Firework','Back'],
                 ])
        bot.sendMessage(chat_id, 'Select element to craft', reply_markup=markup2)
    elif message == 'Foodstuff':
        markup2 = ReplyKeyboardMarkup(keyboard=[
                     ['Bread','Cake','Melon Block','Rabbit Stew','Stew'],
                     ['Golden Apple', 'Enchanted Golden Apple','Back'],
                 ])
        bot.sendMessage(chat_id, 'Select element to craft', reply_markup=markup2)
    elif message == 'Tools':
        markup2 = ReplyKeyboardMarkup(keyboard=[
                     ['Pick','Shovel','Axe', 'Flint and Steel'],
                     ['Sword', 'Hoe','Compass','Clock'],
                     ['Shears', 'Lead','Fishing Rod','Back'],
                 ])
        bot.sendMessage(chat_id, 'Select element to craft', reply_markup=markup2)
    elif message == 'Combat':
        markup2 = ReplyKeyboardMarkup(keyboard=[
                     ['Bow','Arrow','Sword', 'Helmet'],
                     ['Chest', 'Leggings','Boots','Back'],
                 ])
        bot.sendMessage(chat_id, 'Select element to craft', reply_markup=markup2)
    elif message == 'Brewing':
        markup2 = ReplyKeyboardMarkup(keyboard=[
                     ['Brewing Stand','Cauldron','Glass Bottle'],
                     ['Blaze powder', 'Magma cream','Glistering melon',],
                     ['Fermented Spider eye', 'Back'],
                 ])
        bot.sendMessage(chat_id, 'Select element to craft', reply_markup=markup2)
    elif message == 'Materials':
        markup2 = ReplyKeyboardMarkup(keyboard=[
                     ['Stick','Bowl','Leather'],
                     ['Brick', 'Melon seeds','Pumpkin seed',],
                     ['Blazerod', 'Nether brick','Back'],
                 ])
        bot.sendMessage(chat_id, 'Select element to craft', reply_markup=markup2)
    else:
        message = message.lower()
        message = message.replace(" ","")
	similar(message,message);
        if os.path.exists("images/" + message + ".png"):
            f = open("images/" + message + ".png",'rb')
            bot.sendPhoto(chat_id, f)
        elif os.path.exists("images/" + message + ".gif"):
            f = open("images/" + message + ".gif",'rb')
            bot.sendDocument(chat_id, f)
        else:
            bot.sendMessage(chat_id, 'No element existing in our current database')
                


TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)


print 'Listening ...'

# Keep the program running.
while 1:
    time.sleep(10)
